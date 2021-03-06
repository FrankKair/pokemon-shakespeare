from functools import lru_cache
import requests
from .models import Pokemon, decode
from .error import PokemonNotFoundError


BASE_ENDPOINT = 'https://pokeapi.co/api/v2/'
SPECIES_ENDPOINT = BASE_ENDPOINT + 'pokemon-species/'


@lru_cache(maxsize=16)
def get_pokemon(pkm_name: str) -> Pokemon:
    """ Given a pokemon name, returns a Pokemon object.

    Args:
        pkm_name: str

    Returns:
        Pokemon object with name and flavor_text_entries

    Raises:
        PokemonNotFoundError if request times out or Pokemon does not exist
    """
    try:
        url = SPECIES_ENDPOINT + pkm_name
        response = requests.get(url, timeout=5)

    except requests.exceptions.Timeout:
        raise PokemonNotFoundError(f"{pkm_name} not found")

    if response.status_code == 404:
        raise PokemonNotFoundError(f"{pkm_name} not found")

    data = response.json()
    pokemon = decode(data)
    return pokemon
