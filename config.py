import os
import sys
import pathlib
import logging
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.inference.tracing import AIInferenceInstrumentor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

def get_logger(module_name):
    """Returns a module-specific logger"""
    return logging.getLogger(f"app.{module_name}")

def enable_telemetry(log_to_project: bool = False):
    """Enable instrumentation and telemetry logging"""
    AIInferenceInstrumentor().instrument()
    
    # Enable logging message contents
    os.environ["AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED"] = "true"
    
    if log_to_project:
        from azure.monitor.opentelemetry import configure_azure_monitor
        
        project = AIProjectClient.from_connection_string(
            conn_str=os.environ["AIPROJECT_CONNECTION_STRING"],
            credential=DefaultAzureCredential()
        )
        
        application_insights_connection_string = project.telemetry.get_connection_string()
        if application_insights_connection_string:
            configure_azure_monitor(connection_string=application_insights_connection_string)
            logger.info("Telemetry enabled - view traces in Azure AI Foundry")

def get_project_client():
    """Get authenticated project client"""
    return AIProjectClient.from_connection_string(
        conn_str=os.environ["AIPROJECT_CONNECTION_STRING"],
        credential=DefaultAzureCredential()
    )