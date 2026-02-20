import requests
import sys

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    #print(response)

    if response.status_code == 200:
        print("Data retrieved!")
        pokemon_data = response.json()
        return pokemon_data
    elif response.status_code == 404:
        print(f"Failed to retrieve data. Code: {response.status_code}. Try again")
        return False
    else:
        print (f"Error. An unexpected API error occured. {response.status_code}")
        return False


start_pokemon_search = input("Welcome to the PokeApi Search engine. Would you like to " \
"search for a pokemon's information? (Y/N) ")

if start_pokemon_search == 'Y' or start_pokemon_search == 'y':
    pokemon_name = input("What pokemon would you like information on? ")

elif start_pokemon_search == 'N' or start_pokemon_search == 'n':
    print("No problem. Have a good day.")
    sys.exit()
    
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Base Experience: {pokemon_info['base_experience']}")

    
    