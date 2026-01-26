import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    #print(response)

    if response.status_code == 200:
        print("Data retrieved!")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retireve data {response.status_code}")

pokemon_name = "machoke"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Base Experience: {pokemon_info['base_experience']}")
    
    