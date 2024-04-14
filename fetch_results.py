import requests
import json

#set api token
API_TOKEN = 'apify_api_0J2LWMjslSPvviUjlQFKdaMmVcttm64E985F'

#to access the data, import the id of the dataset gotten as a result of apify_api.py
with open('dataset_id.json', 'r') as file:
    dataset_id = json.load(file)['dataset_id']

def fetch_results(dataset_id):
    url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={API_TOKEN}&clean=true&format=json&fields=url,text"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code, response.text)
        return None

#usage
results = fetch_results(dataset_id)
if results:
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("Data fetched and saved successfully!")
else:
    print("Failed to fetch data from dataset")
