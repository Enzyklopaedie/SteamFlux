from traceback import print_last

from bs4 import BeautifulSoup
import stfmaster
import requests
import re


from stfmaster import insert_item

website_to_scrape = "https://store.steampowered.com"

# parse and save robots.txt
disallow_scraping = requests.get(f"{website_to_scrape}/robots.txt")
robots_txt = disallow_scraping.text
disallowed_urls = []

for line in robots_txt.splitlines():
    if line.startswith("Disallow: "):
        subdir = line[10:].strip()                              # should get text after "Disallow: " (10 characters)
        disallowed_urls.append(subdir)



# discover games
game_urls = []



def scrape_game_price():
    for game_url in game_urls:
        response = requests.get(game_url)
        soup = BeautifulSoup(response.text, "html.parser")
        price = soup.find_all("div",{"class":"game_purchase_price price"})
        print(price)



# crawl_games()
scrape_game_price()

