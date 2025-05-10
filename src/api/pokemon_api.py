import requests

class PokemonAPI:
    BASE_URL = "https://pokeapi.co/api/v2"

    def get_pokemon(self, name):
        response = requests.get(f"{self.BASE_URL}/pokemon/{name}")
        return response.json()

    def get_pokemon_by_id(self, pokemon_id):
        response = requests.get(f"{self.BASE_URL}/pokemon/{pokemon_id}")
        return response.json()

    def get_all_pokemons(self, limit=100, offset=0):
        response = requests.get(f"{self.BASE_URL}/pokemon", params={"limit": limit, "offset": offset})
        return response.json()

    def fetch_all_pokemons(self):
        response = requests.get(f"{self.BASE_URL}/pokemon?limit=100")
        response.raise_for_status()  # Lanza una excepción si la solicitud falla
        data = response.json()  # Asegúrate de que la respuesta sea un JSON válido
        if 'results' not in data:
            raise ValueError("Unexpected response format: 'results' key not found")
        return data['results']