import pytest
from unittest.mock import MagicMock
from src.services.pokemon_service import PokemonService

def test_fetch_all_pokemons():
    mock_api = MagicMock()
    mock_api.fetch_all_pokemons.return_value = [{"name": "Pikachu"}, {"name": "Charmander"}]
    service = PokemonService(mock_api)

    result = service.fetch_all_pokemons()

    assert len(result) == 2
    assert result[0]["name"] == "Pikachu"
    assert result[1]["name"] == "Charmander"