# Store-to-File Master module

def insert_item(url):
    url = url + "\n"
    try:
        with open("output_file.txt", 'a', encoding='utf-8') as file:
            file.write(url)
    except Exception as e:
        print(e)