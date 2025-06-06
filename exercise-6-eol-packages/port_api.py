import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
PORT_API_URL = "https://api.port.io/v1"
API_TOKEN = os.getenv("YOUR_PORT_API_TOKEN")

# HTTP headers with authorization
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Blueprint IDs
SERVICE_BLUEPRINT_ID = "service"
FRAMEWORK_BLUEPRINT_ID = "framework"

def get_entities(blueprint_id):
    """
    Fetches all entities for a given blueprint.
    """
    url = f"{PORT_API_URL}/blueprints/{blueprint_id}/entities"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('entities', [])

def get_entity(blueprint_id, entity_id):
    """
    Fetches details for a single entity by blueprint and ID.
    """
    url = f"{PORT_API_URL}/blueprints/{blueprint_id}/entities/{entity_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def update_entity_property(entity_id, property_key, value):
    """
    Updates a single property on an entity.
    """
    url = f"{PORT_API_URL}/entities/{entity_id}"
    data = {
        "properties": {
            property_key: value
        }
    }
    response = requests.patch(url, json=data, headers=HEADERS)
    response.raise_for_status()
    print(f"Updated entity '{entity_id}' with {property_key} = {value}")

def main():
    # Fetch all service entities
    services = get_entities(SERVICE_BLUEPRINT_ID)

    for service in services:
        service_id = service['identifier']
        
        # Fetch detailed info about the service to get relations
        service_detail = get_entity(SERVICE_BLUEPRINT_ID, service_id)

        # Get related frameworks from the 'used_frameworks' relation
        frameworks = service_detail.get('relations', {}).get('used_frameworks', [])
        eol_count = 0

        # Count how many related frameworks are marked as 'EOL'
        for framework in frameworks:
            framework_id = framework['identifier']
            framework_detail = get_entity(FRAMEWORK_BLUEPRINT_ID, framework_id)
            state = framework_detail.get('properties', {}).get('state', '')
            if state == "EOL":
                eol_count += 1

        # Update the service entity with the count of EOL packages
        update_entity_property(service_id, "number_of_eol_packages", eol_count)

if __name__ == "_main_":
    main()