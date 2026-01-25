import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch
)
from dotenv import load_dotenv

load_dotenv()

def create_unified_search_index():
    """Create Azure AI Search index for BOTH ADLS documents AND web content"""
    
    # Connection using API key (works with NEW Foundry)
    search_endpoint = os.environ["AISEARCH_ENDPOINT"]
    search_key = os.environ["AISEARCH_KEY"]
    
    index_client = SearchIndexClient(
        endpoint=search_endpoint,
        credential=AzureKeyCredential(search_key)
    )
    
    index_name = os.environ["AISEARCH_INDEX_NAME"]
    
    # Define index schema with source type
    fields = [
        SearchField(name="id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True),
        SearchField(name="content", type=SearchFieldDataType.String, searchable=True),
        SearchField(name="title", type=SearchFieldDataType.String, searchable=True, filterable=True, sortable=True),
        SearchField(name="source_type", type=SearchFieldDataType.String, filterable=True, facetable=True),
        SearchField(name="source_path", type=SearchFieldDataType.String, filterable=True),
        SearchField(name="url", type=SearchFieldDataType.String, filterable=True),
        SearchField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_profile_name="myHnswProfile"
        )
    ]
    
    # Configure vector search
    vector_search = VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="myHnsw")],
        profiles=[VectorSearchProfile(name="myHnswProfile", algorithm_configuration_name="myHnsw")]
    )
    
    # Configure semantic search
    semantic_config = SemanticConfiguration(
        name="my-semantic-config",
        prioritized_fields=SemanticPrioritizedFields(
            title_field=SemanticField(field_name="title"),
            content_fields=[SemanticField(field_name="content")]
        )
    )
    
    semantic_search = SemanticSearch(configurations=[semantic_config])
    
    # Create index
    index = SearchIndex(
        name=index_name,
        fields=fields,
        vector_search=vector_search,
        semantic_search=semantic_search
    )
    
    print(f"Creating unified search index: {index_name}")
    result = index_client.create_or_update_index(index)
    print(f"✓ Index created: {result.name}")
    
    return result

if __name__ == "__main__":
    create_unified_search_index()
    print("\n✓ Unified search index created successfully!")
    print("  - Ready for ADLS files")
    print("  - Ready for web content")