import requests
import pandas as pd

#api key and url defined
api_key = 'set_api_key'
url = 'https://newsapi.org/v2/everything'

#api request parameters set
params = {
    'q': 'insert_desired_keyword_search',  #query for desired_keyword_search
    'sortBy': 'popularity',  #e.g. sorting by 'popularity'
    'language': 'en',  #lang of the articles parced
    'apiKey': api_key
}

#api request sent
response = requests.get(url, params=params)
data = response.json()

#check status
if data['status'] == 'ok':
    #extract the data
    articles = data['articles']
    articles_data = []

    for article in articles:
        #removing quotes and newlines in 'author' field
        author = article.get('author', 'N/A').replace('\n', ' ').replace('“', '"').replace('”', '"') if article.get(
            'author') else 'N/A'
        #same for 'description' field
        description = article['description'].replace('\n', ' ').replace('“', '"').replace('”', '"')

        articles_data.append({
            'Title': article['title'],
            'Author': author,
            'PublishedAt': article['publishedAt'],
            'Description': description,
            'URL': article['url']
        })

    #dataframe created and saved as
    df_articles = pd.DataFrame(articles_data)
    df_articles.to_csv('set_desired_path',
                       index=False,
                       encoding='utf-8',
                       quotechar='"',
                       quoting=1) 

    print("Articles have been successfully saved to CSV.")
else:
    print("Failed to fetch articles: ", data.get('message', 'No error message available'))
