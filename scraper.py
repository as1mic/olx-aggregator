import requests
import time
import sys

from bs4 import BeautifulSoup
from db import save_ad_to_db, get_all_ads

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

links = []

def fetch_with_retry(url, retries=3, timeout=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=timeout)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"Request error {url}: {e}")
            time.sleep(1)
    return None


def find_all_ads_url(category_url):
    return category_url


main_url = "https://www.olx.pl/"
response = fetch_with_retry(main_url)

if response:
    soup = BeautifulSoup(response.text, "html.parser")
    category_tags = soup.find_all("a", attrs={"data-testid": lambda v: v and v.startswith("cat-")})

    for tag in category_tags:
        href = tag.get("href")
        if href and href.startswith("/"):
            full_url = "https://www.olx.pl" + href
            links.append(full_url)


def parse_ads(url):
    response = fetch_with_retry(url)
    if not response:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    ads = soup.select('div[data-cy="l-card"]')

    for ad in ads:
        title_tag = ad.select_one('div[data-cy="ad-card-title"]')
        title = title_tag.text.strip() if title_tag else "–"

        link_tag = ad.select_one('a[href]')
        link = "https://www.olx.pl" + link_tag.get('href') if link_tag else "–"

        price_tag = ad.select_one('div.css-odp1qd')
        price = price_tag.text.strip() if price_tag else "–"

        save_ad_to_db(title, price, link)


for category in links:
    print(f"Category: {category}")
    ads_url = find_all_ads_url(category)
    if ads_url: 
        print(f"All propositions: {ads_url}\n")
        parse_ads(full_url)
    else:
        print("No propositions\n")


def read_saved_ads():
    print("\nAds from the database:")
    ads = get_all_ads()
    for title, price, link in ads:
        print(f"{title} | {price} | {link}")


read_saved_ads()

