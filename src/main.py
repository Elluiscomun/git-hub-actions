import requests
from api.pokemon_api import PokemonAPI
from services.pokemon_service import PokemonService

def main():
    pokemon_api = PokemonAPI()
    pokemon_service = PokemonService(pokemon_api)

    try:
        print("Fetching all Pokémon...")
        all_pokemons = pokemon_service.fetch_all_pokemons()

        if not all_pokemons:
            print("No Pokémon data found.")
            return

        print("List of Pokémon:")
        for pokemon in all_pokemons:
            print(f"- {pokemon['name']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching Pokémon data: {e}")
    except KeyError as e:
        print(f"Unexpected data format: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()