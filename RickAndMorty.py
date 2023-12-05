import requests

# Перое задание
def get_character_count():
    urlRickAndMorty = "https://rickandmortyapi.com/api/character"
    response = requests.get(urlRickAndMorty)
    result = response.json()
    characters_count = result["info"]["count"]
    return characters_count
