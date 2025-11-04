import re
import requests
import stfmaster
from main import website_to_scrape


game_urls = []

def crawl_games(filename="game_urls.txt", game_id=10):
    remove_duplicates_from_games_file(filename)                 # prevent getting value of website_to_scrape as response
    status_ok = 0

    while status_ok < 5:
        game = requests.get(f"{website_to_scrape}/app/{game_id}")
        print(game)
        if game.status_code != 200:
            status_ok += 1
        else:
            game_urls.append(game.url)
            stfmaster.insert_item(game.url, filename)                      # storing the games to a file
            print(f"ID: {game_id} was added successfully.")
            status_ok = 0
        game_id += 10


# Extracting last item from file, getting its game id
# and using it as seed for crawl_games()
def get_start_game_id_for_next_crawl(filename="game_urls.txt"):
    remove_duplicates_from_games_file()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            saved_urls = file.read().splitlines()
            try:
                last_line = saved_urls[len(saved_urls) - 1]
            except IndexError:
                crawl_games(filename)
                print("File empty. Starting new crawl..")
            try:
                extracted_game_id = int(re.search(r'/app/(\d+)', last_line).group(1))
                print("Last line is: ", last_line, "\nGame ID: ", extracted_game_id, f"\nNew Start-ID for crawler: {extracted_game_id + 10}")
                extracted_game_id = extracted_game_id + 10          # 10 is the default increment for giving out Game IDs
                                                                    # by Valve for games on Steam
            except AttributeError:
                crawl_games(filename)
                print("File not parsable. Starting new crawl..")
    except FileNotFoundError:
        print("No existing crawled urls found.")
        extracted_game_id = 10

    crawl_games(filename, extracted_game_id)


def remove_duplicates_from_games_file(filename="game_urls.txt"):
    games_index = []
    with open(filename, "r") as file:
        games_list = file.read().splitlines()
    for game_url in games_list:
        if game_url == website_to_scrape + "/":
            games_list.remove(game_url)
    with open(filename, "w") as file:
        file.write("\n".join(games_list))



def crawling(filename="game_urls.txt"):
    try:
        with open(filename, 'w', encoding='utf-8'):
            pass
        get_start_game_id_for_next_crawl(filename)
        print("Continuing last crawl..")
    except FileNotFoundError or AttributeError:
        crawl_games(filename)
        print("Starting new crawl..")

crawling("game_urls.txt")