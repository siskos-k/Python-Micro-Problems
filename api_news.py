api_key = "your key"
import requests
import os


response = requests.get('https://newsapi.org/v2/top-headlines',
                        params={'country': 'us', 'apiKey': api_key},
                        headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    data = response.json()
    headlines = data['articles']
    for headline in headlines:
        print(f"Title: {headline['title']}")
        print(f"Description: {headline['description']}")
        print(f"URL: {headline['url']}")
        print()

    # Process the response
else:
    print('Error: Unable to get news headlines')
