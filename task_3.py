import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0 (compatible; Python Web Scraper/1.0)"}
response = requests.get(URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all(["h2", "h3"])
headline_texts = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]
with open("headlines.txt", "w", encoding="utf-8") as f:
    for line in headline_texts:
        f.write(line + "\n")
print(f"Extracted {len(headline_texts)} headlines to headlines.txt")
