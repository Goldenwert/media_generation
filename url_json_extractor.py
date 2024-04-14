import pandas as pd
import json

#load data contained article
data = pd.read_csv('set_path_of_aricles.csv')

#urls extracted and prepared as .json with semicolon as a sep
urls = data['URL'].tolist()
json_data = {'urls': urls}

#file written
with open('urls.json', 'w') as json_file:
    json.dump(json_data, json_file)

print("URLs have been extracted and saved to urls.json")
