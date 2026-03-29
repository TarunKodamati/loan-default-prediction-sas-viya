import requests
import urllib3
urllib3.disable_warnings()

# Try different client IDs
client_ids = ["sas.ec", "app", "SASApp", "SASLogon"]

url = "https://vfl-026.engage.sas.com/SASLogon/oauth/token"

for client_id in client_ids:
    print(f"\nTrying client_id: {client_id}")
    
    data = {
        "grant_type": "password",
        "username": "tkodamati",
        "password": "Sra37342@123",
        "client_id": client_id,
        "client_secret": ""
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    
    response = requests.post(
        url, 
        headers=headers, 
        data=data, 
        verify=False
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if "access_token" in response.text:
        print(f"\nSUCCESS! client_id = {client_id}")
        print(f"Token: {response.json()['access_token']}")
        break