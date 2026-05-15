import pandas as pd

def transform_data(scraped, api_data):
    df = pd.DataFrame(scraped)

    df["base_currency"] = api_data["base"]
    df["PKR_rate"] = api_data["rate_PKR"]

    return df