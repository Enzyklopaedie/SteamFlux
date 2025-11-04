import requests
import stfmaster
from main import website_to_scrape


game_urls = []

def crawl_games():
    status_ok = 0
    game_id = 10



    while status_ok < 5:
        game = requests.get(f"{website_to_scrape}/app/{game_id}")
        print(game)
        if game.status_code != 200:
            status_ok += 1
        else:
            game_urls.append(game.url)
            stfmaster.insert_item(game.url, "game_urls.txt")                      # storing the games to a file
            print(f"ID: {game_id} erfolgreich hinzugefügt.")
            status_ok = 0
        game_id += 10



def remove_duplicates_from_games_file(filename="game_urls.txt"):
    games_index = []
    with open(filename, "r") as file:
        games_list = file.read().splitlines()
    for game_url in games_list:
        if game_url == website_to_scrape + "/":
            games_list.remove(game_url)
    with open(filename, "w") as file:
        file.write("\n".join(games_list))



def crawling():
    return

remove_duplicates_from_games_file(filename="game_urls.txt")