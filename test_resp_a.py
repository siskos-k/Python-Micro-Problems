import requests

google_api_key = "your_google_api_key"
facebook_access_token = "your_facebook_access_token"

def get_google_campaigns():
    url = "https://www.googleapis.com/ads/v10/customers/your_customer_id/campaigns"
    headers = {"Authorization": f"Bearer {google_api_key}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_facebook_campaigns():
    url = "https://graph.facebook.com/v15.0/me/adcampaigns"
    params = {"access_token": facebook_access_token}
    response = requests.get(url, params=params)
    return response.json()

def get_ads_data(api_url, headers):
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

# Example usage
api_url = "https://api.vendor.com/ads/data"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
data = get_ads_data(api_url, headers)
print(data)
# ... (similar functions for other vendors)

google_campaigns = get_google_campaigns()
facebook_campaigns = get_facebook_campaigns()

# Process and store the data
