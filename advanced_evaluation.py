"""
Advanced evaluation using Azure AI Evaluation SDK
"""

from azure.ai.evaluation import evaluate, GroundednessEvaluator, RelevanceEvaluator, CoherenceEvaluator
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()

# Create test dataset (ground truth Q&A pairs)
test_data = [
    {
        "query": "What does MAS regulate?",
        "response": "MAS regulates financial institutions and monetary policy.",  # Expected answer
        "context": "Source documents about MAS regulations"
    },
    {
        "query": "What are the penalties for non-compliance?",
        "response": "Penalties include fines and license revocation.",
        "context": "Source documents about penalties"
    }
]

def run_advanced_evaluation():
    """Run Azure AI Evaluation"""
    
    foundry_endpoint = os.environ["FOUNDRY_ENDPOINT"]
    foundry_key = os.environ["FOUNDRY_KEY"]
    
    # Initialize evaluators
    evaluators = {
        "groundedness": GroundednessEvaluator(
            credential=AzureKeyCredential(foundry_key),
            azure_endpoint=foundry_endpoint
        ),
        "relevance": RelevanceEvaluator(
            credential=AzureKeyCredential(foundry_key),
            azure_endpoint=foundry_endpoint
        ),
        "coherence": CoherenceEvaluator(
            credential=AzureKeyCredential(foundry_key),
            azure_endpoint=foundry_endpoint
        )
    }
    
    # Run evaluation
    results = evaluate(
        data=test_data,
        evaluators=evaluators
    )
    
    print("Evaluation Results:")
    print(f"Groundedness Score: {results['groundedness']}")
    print(f"Relevance Score: {results['relevance']}")
    print(f"Coherence Score: {results['coherence']}")

if __name__ == "__main__":
    run_advanced_evaluation()