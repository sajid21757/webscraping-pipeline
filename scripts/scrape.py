import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        data.append({
            "text": text,
            "author": author
        })

    return data