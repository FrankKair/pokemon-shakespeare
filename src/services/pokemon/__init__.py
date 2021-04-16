from .client import get_pokemon
from .models import Pokemon
from .error import PokemonNotFoundError
from .fixtures import species_charizard, pokemon_charizard, pokemon_charizard_without_desc

fixtures = {
    'species_charizard': species_charizard,
    'pokemon_charizard': pokemon_charizard,
    'pokemon_charizard_without_description': pokemon_charizard_without_desc
}
