class PokemonService:
    def __init__(self, pokemon_api):
        self.pokemon_api = pokemon_api

    def fetch_pokemon_data(self, name):
        return self.pokemon_api.get_pokemon(name)

    def fetch_all_pokemons(self):
        return self.pokemon_api.fetch_all_pokemons()