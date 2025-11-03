"""
# parse game urls
import * from main
website_to_scrape_response = requests.get(website_to_scrape)
soup = BeautifulSoup(website_to_scrape_response.text, "html.parser")
link_tags = soup.find_all("a")

for tag in link_tags:
    if tag:
        game_url = tag.get("href")
        if game_url in disallowed_urls:
            disallowed_urls.remove(game_url)

        print(f"Nice: {game_url}")
    else:
        print("schade")


links = soup.find_all("a",{"data-key":"hover div"})
print(links)
"""