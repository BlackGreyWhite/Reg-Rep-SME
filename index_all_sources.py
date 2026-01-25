"""
Unified indexing script that indexes BOTH:
1. Documents from Azure Data Lake Storage
2. Content from websites
"""

import os
import hashlib
from typing import List, Dict
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
from azure.search.documents import SearchClient
from azure.ai.inference import EmbeddingsClient
from web_scraper import scrape_all_sources
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_blob(blob_client):
    """Extract text from blob (supports PDF, text, and other formats)"""
    try:
        blob_data = blob_client.download_blob()
        content = blob_data.readall()
        
        # Check if it's a PDF
        if blob_client.blob_name.lower().endswith('.pdf'):
            from pypdf import PdfReader
            import io
            
            pdf_file = io.BytesIO(content)
            reader = PdfReader(pdf_file)
            
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            return text
        
        # Try to decode as text
        try:
            text = content.decode('utf-8')
        except:
            text = str(content)
        
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        if chunk:
            chunks.append(chunk)
        
        start = end - overlap
    
    return chunks

def get_embeddings(text, embeddings_client):
    """Generate embeddings for text"""
    response = embeddings_client.embed(
        input=[text],
        model=os.environ["EMBEDDINGS_MODEL"]
    )
    return response.data[0].embedding

def index_adls_documents(embeddings_client, search_client) -> List[Dict]:
    """Index documents from ADLS"""
    print("\n" + "="*80)
    print("INDEXING ADLS DOCUMENTS")
    print("="*80)
    
    # Connection using storage account key
    adls_account = os.environ["ADLS_ACCOUNT_NAME"]
    adls_key = os.environ["ADLS_ACCOUNT_KEY"]
    container_name = os.environ["ADLS_CONTAINER_NAME"]
    
    blob_service_client = BlobServiceClient(
        account_url=f"https://{adls_account}.blob.core.windows.net",
        credential=adls_key
    )
    
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    
    documents = []
    
    for blob in blobs:
        print(f"Processing file: {blob.name}")
        
        blob_client = container_client.get_blob_client(blob.name)
        text = extract_text_from_blob(blob_client)
        
        if not text:
            print(f"Warning: No text extracted from {blob.name}")
            continue
        
        chunks = chunk_text(text)
        
        for i, chunk in enumerate(chunks):
            doc_id = hashlib.md5(f"adls_{blob.name}_{i}".encode()).hexdigest()
            embedding = get_embeddings(chunk, embeddings_client)
            
            doc = {
                "id": doc_id,
                "content": chunk,
                "title": blob.name,
                "source_type": "adls_file",
                "source_path": blob.name,
                "url": blob_client.url,
                "content_vector": embedding
            }
            
            documents.append(doc)
            print(f"  Created chunk {i+1}/{len(chunks)}")
    
    print(f"✓ Prepared {len(documents)} documents from ADLS")
    return documents

def index_web_content(embeddings_client, search_client) -> List[Dict]:
    """Index content from websites"""
    print("\n" + "="*80)
    print("INDEXING WEB CONTENT")
    print("="*80)
    
    max_pages = int(os.getenv("WEB_MAX_PAGES_PER_SITE", 50))
    web_results = scrape_all_sources(max_pages_per_site=max_pages)
    
    if not web_results:
        print("Warning: No web content scraped")
        return []
    
    documents = []
    
    for result in web_results:
        print(f"Processing: {result['title'][:60]}...")
        
        chunks = chunk_text(result['content'])
        
        for i, chunk in enumerate(chunks):
            doc_id = hashlib.md5(f"web_{result['url']}_{i}".encode()).hexdigest()
            embedding = get_embeddings(chunk, embeddings_client)
            
            doc = {
                "id": doc_id,
                "content": chunk,
                "title": result['title'],
                "source_type": "website",
                "source_path": result['url'],
                "url": result['url'],
                "content_vector": embedding
            }
            
            documents.append(doc)
        
        print(f"  Created {len(chunks)} chunks")
    
    print(f"✓ Prepared {len(documents)} documents from web")
    return documents

def index_all_sources():
    """Index ALL sources: ADLS files + Websites"""
    
    # Connection to Foundry models using API key
    foundry_endpoint = os.environ["FOUNDRY_ENDPOINT"]
    foundry_key = os.environ["FOUNDRY_KEY"]
    
    embeddings_client = EmbeddingsClient(
        endpoint=foundry_endpoint,
        credential=AzureKeyCredential(foundry_key)
    )
    
    # Connection to Azure AI Search using API key
    search_endpoint = os.environ["AISEARCH_ENDPOINT"]
    search_key = os.environ["AISEARCH_KEY"]
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=os.environ["AISEARCH_INDEX_NAME"],
        credential=AzureKeyCredential(search_key)
    )
    
    all_documents = []
    
    try:
        adls_docs = index_adls_documents(embeddings_client, search_client)
        all_documents.extend(adls_docs)
    except Exception as e:
        print(f"Error indexing ADLS: {e}")
    
    try:
        web_docs = index_web_content(embeddings_client, search_client)
        all_documents.extend(web_docs)
    except Exception as e:
        print(f"Error indexing web content: {e}")
    
    if all_documents:
        print("\n" + "="*80)
        print(f"UPLOADING {len(all_documents)} TOTAL DOCUMENTS TO INDEX")
        print("="*80)
        
        batch_size = 100
        for i in range(0, len(all_documents), batch_size):
            batch = all_documents[i:i+batch_size]
            result = search_client.upload_documents(documents=batch)
            print(f"Uploaded batch {i//batch_size + 1}: {len(batch)} documents")
        
        print("\n" + "="*80)
        print("✓ INDEXING COMPLETE!")
        print("="*80)
        print(f"Total documents indexed: {len(all_documents)}")
        
        adls_count = sum(1 for d in all_documents if d['source_type'] == 'adls_file')
        web_count = sum(1 for d in all_documents if d['source_type'] == 'website')
        print(f"  - ADLS files: {adls_count}")
        print(f"  - Web pages: {web_count}")
    else:
        print("Warning: No documents to index!")

if __name__ == "__main__":
    index_all_sources()