from functools import lru_cache
import requests
from .models import Pokemon, decode


BASE_ENDPOINT = 'https://pokeapi.co/api/v2/'
SPECIES_ENDPOINT = BASE_ENDPOINT + 'pokemon-species/'


@lru_cache(maxsize=32)
def get_pokemon(pkm_name: str) -> Pokemon:
    url = SPECIES_ENDPOINT + pkm_name
    response = requests.get(url)
    data = response.json()
    pokemon = decode(data)
    return pokemon
