# Store-to-File Master module

def insert_item(url, filename="output_file.txt"):
    url = url + "\n"
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(url)
    except Exception as e:
        print(e)