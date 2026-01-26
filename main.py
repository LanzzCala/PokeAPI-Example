import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    
pokemon_name = "pikachu"
get_pokemon_info(pokemon_name)