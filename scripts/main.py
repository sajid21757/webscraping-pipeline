from scrape import scrape_quotes
from api_fetch import fetch_api_data
from transform import transform_data
from load import load_data

def run_pipeline():
    scraped_data = scrape_quotes()
    api_data = fetch_api_data()
    df = transform_data(scraped_data, api_data)
    load_data(df)

if __name__ == "__main__":
    run_pipeline()