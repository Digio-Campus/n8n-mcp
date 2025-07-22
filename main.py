#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = FastMCP("n8n-utils-server", dependencies=["requests", "os", "dotenv"])

def make_request(endpoint: str, options: dict = None) -> str:
    """
    Make a request to the n8n server.

    :param endpoint: API endpoint path (e.g., '/workflows')
    :param options: Dictionary with request options (method, headers, json, data, params, etc.)
    :return: Response from the server as a string
    """
    url = f"{baseUrl}/api/v1{endpoint}"
    headers = {
      'X-N8N-API-KEY': api_key,
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    }
    
    try:
        # Combinar headers base con headers de options si existen
        combined_headers = {**headers, **options.get('headers', {})}
        
        # Hacer la petición usando requests
        response = requests.request(
            method=options.get('method', 'GET'),
            url=url,
            headers=combined_headers,
            json=options.get('json'),
            data=options.get('data'),
            params=options.get('params'),
            timeout=options.get('timeout')
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Error making request: {str(e)}"

@app.tool()
def list_workflows() -> str:
    """
    List all workflows in the n8n instance.

    :return: JSON string of workflows
    """
    return make_request('/workflows', {
        'method': 'GET',
    })

@app.tool()
def get_workflow(workflow_id: str) -> str:
    """
    Get a specific workflow by ID.

    :param workflow_id: The ID of the workflow to retrieve
    :return: JSON string of the workflow
    """
    return make_request(f'/workflows/{workflow_id}', {
        'method': 'GET',
    })

@app.tool()
def create_workflow(name: str, nodes: list, connections: list) -> str:
    """
    Create a new workflow.

    :param name: The name of the workflow
    :param nodes: The nodes in the workflow
    :param connections: The connections between nodes
    :return: JSON string of the created workflow
    """
    return make_request('/workflows', {
        'method': 'POST',
        'json': {
            'name': name,
            'nodes': nodes,
            'connections': connections,
            'settings': {
                'saveExecutionProgress': True,
                'saveManualExecutions': True
            }
        }
    })

@app.tool()
def update_workflow(workflow_id: str, name: str, nodes: list, connections: list) -> str:
    """
    Update an existing workflow.

    :param workflow_id: The ID of the workflow to update
    :param name: The new name of the workflow
    :param nodes: The updated nodes in the workflow
    :param connections: The updated connections between nodes
    :return: JSON string of the updated workflow
    """
    return make_request(f'/workflows/{workflow_id}', {
        'method': 'PUT',
        'json': {
            'name': name,
            'nodes': nodes,
            'connections': connections,
            'settings': {
                'saveExecutionProgress': True,
                'saveManualExecutions': True
            }
        }
    })

if __name__ == "__main__":
    baseUrl = os.getenv("N8N_URL", "http://localhost:5678")
    api_key = os.getenv("N8N_API_KEY")
    app.run(transport="stdio")
