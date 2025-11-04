import requests
from bs4 import BeautifulSoup
def get_games():
    status_ok = 0
    game_id = 10
    game_urls = []

    while status_ok < 5:
        game = requests.get(f"https://store.steampowered.com/app/{game_id}")
        print(game)
        if game.status_code != 200:
            status_ok += 1

        else:
            game_urls.append(game.url)
            print(f"ID: {game_id} erfolgreich hinzugefügt")
            status_ok = 0
        game_id += 10

def looking_around():
    response = requests.get(f"https://store.steampowered.com/app/10")
    print(response.text)
