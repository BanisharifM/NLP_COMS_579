import requests

# Constants (fill with actual data or securely retrieve them)
USERNAME = "your_username"
PASSWORD = "your_password"
AUTH_URL = "https://your-wcs-domain.com/auth"
CLUSTER_CREATE_URL = "https://your-wcs-domain.com/create_cluster"


# Function to get an API token
def get_api_token(username, password):
    response = requests.post(
        AUTH_URL, json={"username": username, "password": password}
    )
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()["access_token"]


# Function to create a cluster
def create_cluster(token):
    headers = {"Authorization": f"Bearer {token}"}
    # Customize your payload as per API specification
    payload = {"cluster_config": {"region": "us-west1", "configuration": "basic"}}
    response = requests.post(CLUSTER_CREATE_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


# Main function to handle the workflow
def main():
    try:
        token = get_api_token(USERNAME, PASSWORD)
        cluster_info = create_cluster(token)
        print("Cluster created successfully:", cluster_info)
    except requests.HTTPError as e:
        print("Failed to create cluster:", e)


# Run the main function
if __name__ == "__main__":
    main()
