from bs4 import BeautifulSoup
import stfmaster
import requests

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

def crawl_games():
    status_ok = 0
    game_id = 10

    while status_ok < 5:
        #
        game = requests.get(f"https://store.steampowered.com/app/{game_id}")
        print(game)
        if game.status_code != 200:
            status_ok += 1
        else:
            game_urls.append(game.url)
            print(f"ID: {game_id} erfolgreich hinzugefügt")
            status_ok = 0
        game_id += 10

def scrape_game_prices():
    return
    # some code for retrieving the prices idk