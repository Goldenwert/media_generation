import requests
import pandas as pd

# Define API key and endpoint
api_key = '026e53bb60454e38b619db9fa09e7996'
url = 'https://newsapi.org/v2/everything'

# Set up parameters for the API request
params = {
    'q': 'skincare trends',  # Query for trending skincare topics
    'sortBy': 'popularity',  # Sort by publication date
    'language': 'en',  # Filter articles written in English
    'apiKey': api_key
}

# Send the request to the News API
response = requests.get(url, params=params)
data = response.json()

# Check if the API call was successful and data is received
if data['status'] == 'ok':
    # Extract articles
    articles = data['articles']

    # Prepare a list to hold all article data
    articles_data = []
    for article in articles:
        # Clean up the Author field to remove newlines and quotes
        author = article.get('author', 'N/A').replace('\n', ' ').replace('“', '"').replace('”', '"') if article.get(
            'author') else 'N/A'
        # Clean up the Description field to remove newlines and extra quotes
        description = article['description'].replace('\n', ' ').replace('“', '"').replace('”', '"')

        articles_data.append({
            'Title': article['title'],
            'Author': author,
            'PublishedAt': article['publishedAt'],
            'Description': description,
            'URL': article['url']
        })



    # Create a DataFrame
    df_articles = pd.DataFrame(articles_data)

    # Save the DataFrame to a CSV file, ensuring UTF-8 encoding and proper quoting
    df_articles.to_csv('C:/Users/garim/OneDrive/Рабочий стол/project/skincare_trends_articles.csv',
                       index=False,
                       encoding='utf-8',
                       quotechar='"',
                       quoting=1)  # quoting=1 is for csv.QUOTE_ALL

    print("Articles have been successfully saved to CSV.")
else:
    print("Failed to fetch articles: ", data.get('message', 'No error message available'))
