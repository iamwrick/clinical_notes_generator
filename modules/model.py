"""
Configuration and AWS Interaction Module

This module provides functionality related to loading configuration data from a JSON file and interacting with AWS services.

Attributes:
    project_root (str): The root directory of the project.
    config_file_path (str): The path to the config.json file.

Functions:
    query_bedrock_sonet(prompt):
        Query the Bedrock SONET model with the provided prompt.
"""

import json
import os
import boto3
from modules.utils import load_config_data

# Get the path to the config.json file
project_root = os.path.dirname(os.path.dirname(__file__))  # Navigate 2 levels up from the script directory
config_file_path = os.path.join(project_root, 'config.json')


def query_bedrock_sonet(prompt):
    """
    Query the Bedrock SONET model with the provided prompt.

    Args:
        prompt (str): The prompt to query the Bedrock SONET model.

    Returns:
        dict: Response from the Bedrock SONET model.
    """
    # Load the AWS credentials data
    aws_credentials = load_config_data(config_file_path)
    region = aws_credentials['region']

    # Initialize the Bedrock client
    bedrock = boto3.client(
        service_name="bedrock-runtime", region_name=region
    )
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Invoke the Bedrock SONET model
    response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 4086,
                "messages": [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}],
                    }
                ],
            }
        ),
    )

    # Process and return the response
    result = json.loads(response.get("body").read())
    return result
