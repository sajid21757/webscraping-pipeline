import requests

def fetch_api_data():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()

    return {
        "base": data["base"],
        "rate_PKR": data["rates"]["PKR"]
    }