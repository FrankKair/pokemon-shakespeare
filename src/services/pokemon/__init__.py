from .client import get_pokemon
from .models import Pokemon


def fixtures():
    from .fixtures import species_charizard, pokemon_charizard, pokemon_charizard_without_desc
    return {
        'species_charizard': species_charizard,
        'pokemon_charizard': pokemon_charizard,
        'pokemon_charizard_without_description': pokemon_charizard_without_desc
    }
