import requests
import json

#set api token
API_TOKEN = 'apify_api_0J2LWMjslSPvviUjlQFKdaMmVcttm64E985F'

#set id of the apify-actor
ACTOR_ID = 'aYG0l9s7dbB7j3gbS'

#apify headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_TOKEN}',
}

#prepare input file of urls
with open('urls.json', 'r') as file:
    urls = json.load(file)['urls']

#actor settings
actor_input = {
    "startUrls": [{"url": url} for url in urls],
    "maxCrawlDepth": 20,
    "maxPages": 100,
    # "initialConcurrency": value,
    "maxConcurrency": 200,
    "saveHtml": False,
    "saveMarkdown": True,
    "saveFiles": False,
    "saveScreenshots": False,
    "maxResults": 100,
    "proxyConfiguration": {
        "useApifyProxy": True
    },
    "crawlerType": "cheerio"  #raw-http client possesses itself as 'High-performance mode using raw HTTP requests.
    #It is faster and cheaper, but it might not work on all websites.
}

#run the actor
url = f'https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={API_TOKEN}'

#POST request for the start
response = requests.post(url, headers=headers, json=actor_input)

if response.status_code == 201:
    run_data = response.json()
    dataset_id = run_data['data']['defaultDatasetId']

    #save the id of the dataset in .json file for the next step
    with open('dataset_id.json', 'w') as f:
        json.dump({'dataset_id': dataset_id}, f)

    print("Actor started successfully!")
    print("Dataset ID:", dataset_id)
    print("Dataset ID saved to dataset_id.json")
else:
    print("Failed to start actor:", response.status_code, response.text)
