from functools import lru_cache
from .shakespeare_client import shakespeare_translation
from .pokemon_client import pokemon_description


@lru_cache(maxsize=32)
def pokemon_shakespeare_description(pokemon: str) -> str:
    desc = pokemon_description(pokemon)
    translation = shakespeare_translation(desc)
    return translation

