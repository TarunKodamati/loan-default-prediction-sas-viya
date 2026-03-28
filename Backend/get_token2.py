import requests
import urllib3
urllib3.disable_warnings()

# Okta-based SAS auth
urls_to_try = [
    "https://vfl-026.engage.sas.com/SASLogon/oauth/token",
    "https://vfl-026.engage.sas.com/SASLogon/v1/tickets",
    "https://vfl-026.engage.sas.com/auth/oauth/token",
]

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

data = {
    "grant_type": "password",
    "username": "tkodamati@uco.edu",
    "password": "Sra37342@123",
    "client_id": "sas.ec",
    "client_secret": ""
}

for url in urls_to_try:
    print(f"\nTrying: {url}")
    try:
        r = requests.post(url, headers=headers, data=data, verify=False)
        print(f"Status: {r.status_code}")
        print(f"Response: {r.text[:200]}")
        if "access_token" in r.text:
            print(" FOUND TOKEN!")
            break
    except Exception as e:
        print(f"Error: {e}")

print("\nDone!")