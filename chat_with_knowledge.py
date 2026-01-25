import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from dotenv import load_dotenv

load_dotenv()

def search_documents(query, search_client, top=5):
    """Search for relevant documents from ALL sources"""
    results = search_client.search(
        search_text=query,
        top=top,
        select=["content", "title", "source_type", "source_path", "url"]
    )
    
    documents = []
    for result in results:
        documents.append({
            "content": result["content"],
            "title": result["title"],
            "source_type": result["source_type"],
            "source_path": result["source_path"],
            "url": result.get("url", "")
        })
    
    return documents

def create_context_from_documents(documents):
    """Create context string from retrieved documents"""
    context_parts = []
    
    for i, doc in enumerate(documents, 1):
        source_label = "FILE" if doc['source_type'] == 'adls_file' else "WEB"
        # Limit content length per source to avoid overwhelming the model
        content = doc['content'][:1000]  # First 1000 chars only
        context_parts.append(
            f"[Source {i} - {source_label}: {doc['title']}]\n{content}\n"
        )
    
    return "\n---\n".join(context_parts)  # Clear separator between sources

def chat_with_rag(query, show_sources=True):
    """Main RAG chat function with mixed sources"""
    
    # Connection to Azure AI Search using API key
    search_endpoint = os.environ["AISEARCH_ENDPOINT"]
    search_key = os.environ["AISEARCH_KEY"]
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=os.environ["AISEARCH_INDEX_NAME"],
        credential=AzureKeyCredential(search_key)
    )
    
    # Connection to Foundry models using API key
    foundry_endpoint = os.environ["FOUNDRY_ENDPOINT"]
    foundry_key = os.environ["FOUNDRY_KEY"]
    chat_client = ChatCompletionsClient(
        endpoint=foundry_endpoint,
        credential=AzureKeyCredential(foundry_key)
    )
    
    print(f"Searching knowledge base for: {query}")
    documents = search_documents(query, search_client)
    
    if not documents:
        print("Warning: No relevant documents found")
        return "I couldn't find any relevant information to answer your question."
    
    context = create_context_from_documents(documents)
    
    adls_sources = sum(1 for d in documents if d['source_type'] == 'adls_file')
    web_sources = sum(1 for d in documents if d['source_type'] == 'website')
    
    print(f"Found {len(documents)} relevant sources ({adls_sources} files, {web_sources} web pages)")
    
    system_prompt = """Answer questions using the information provided in the sources below.

Example:
Question: What regulations does MAS enforce?
Sources: "MAS enforces financial regulations and monetary policy..."
Answer: According to Source 1, MAS enforces financial regulations and oversees monetary policy in Singapore.

Now answer the user's question using the same approach.

Sources:
{context}

Question: {question}

Provide a clear, helpful answer and cite the source number(s).
"""
    
    messages = [
        SystemMessage(content=system_prompt.format(context=context, question=query)),
        UserMessage(content=query)
    ]
    
    print("Generating response with GPT-5-mini...")
    response = chat_client.complete(
        model=os.environ["CHAT_MODEL"],
        messages=messages
    )
    
    answer = response.choices[0].message.content
    
    print("\n" + "="*80)
    print("ANSWER:")
    print("="*80)
    print(answer)
    
    # Only show sources if we have a real answer (not "I don't know" response)
    if show_sources and not any(phrase in answer.lower() for phrase in [
        "don't have", "couldn't find", "no information", "don't know", "unable to", 
        "can't find", "cannot find", "no relevant"
    ]):
        print("\n" + "="*80)
        print("SOURCES:")
        print("="*80)
        for i, doc in enumerate(documents, 1):
            icon = "📄" if doc['source_type'] == 'adls_file' else "🌐"
            print(f"{i}. {icon} {doc['title']}")
            print(f"   {doc['url'] or doc['source_path']}")
        print("="*80 + "\n")
    
    return answer

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Question to ask")
    parser.add_argument("--no-sources", action="store_true", help="Don't show sources")
    
    args = parser.parse_args()
    
    chat_with_rag(args.query, not args.no_sources)