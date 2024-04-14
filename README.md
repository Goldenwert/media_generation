# Media Generation Project

This repository is home to a suite of Python scripts that automate the collection, parsing, and summarization of trending skincare articles. By leveraging news APIs, web scraping, and natural language processing, this project streamlines the extraction of article content for subsequent content generation or analytical endeavors.

## Project Structure

- **news_api_parcer.py**
  - Retrieves news articles related to a specified keyword via an API key.
  - Articles are searched and sorted according to user preferences, such as popularity.
  - Results are saved in CSV format (`sample_articles.csv`).

- **urls_json_extractor.py**
  - Extracts URLs from the `sample_articles.csv` and saves them to a JSON file (`urls.json`).

- **Apify Actor Integration**
  - Invokes an Apify Actor through an API token to fetch textual content from article URLs.
  - The output is `dataset_id.json`, which includes the necessary dataset ID for further actions.

- **fetch_results.py**
  - Uses the dataset ID from `dataset_id.json` to access the Apify dataset.
  - Retrieves article texts and URLs, storing them in `results.json`.

- **results.json**
  - A JSON file containing the article texts and corresponding URLs, ready for rephrasing and editing.

- **To Be Continued**
  - Ongoing project enhancements will incorporate NLP techniques for content summarization and integration with content management systems.
  - Currently under development.

## How to Use

To utilize the scripts for data collection:

1. Install required Python packages as listed in `requirements.txt`.
2. Configure your API keys and tokens within a `.env` file or directly within the scripts (not recommended for security reasons).
3. Execute `news_api_parcer.py` to start the collection of articles.
4. Run `urls_json_extractor.py` to compile article URLs into a JSON file.
5. Activate the Apify Actor with your API token to retrieve content from the articles.
6. Use `fetch_results.py` to access the complete set of articles' data.

## Future Work

- Integration with an NLP service or the development of a custom model for the summarization of content.
- Implementation of automated rephrasing and editing functionalities for the article content.

## Contribution

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

