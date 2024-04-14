import pandas as pd
import json

# Load the CSV file
data = pd.read_csv('C:/Users/garim/OneDrive/Рабочий стол/project/skincare_trends_articles.csv')

# Extract URLs into a list
urls = data['URL'].tolist()

# Prepare JSON data
json_data = {'urls': urls}

# Write to a JSON file
with open('urls.json', 'w') as json_file:
    json.dump(json_data, json_file)

print("URLs have been extracted and saved to urls.json")
