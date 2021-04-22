import responses
from .models import decode
from .client import get_pokemon
from .error import PokemonNotFoundError
from ...fixtures import species_charizard, pokemon_charizard


URL = 'https://pokeapi.co/api/v2/pokemon-species/'


def test_pokemon_decoder():
    result = decode(species_charizard)
    assert result == pokemon_charizard


def test_pokemon_decoder_fail_empty():
    try:
        _ = decode({})
    except PokemonNotFoundError:
        assert True


def test_pokemon_decoder_fail_bad_json():
    try:
        _ = decode({'data': 'hello', 'data2': 'hello2'})
    except PokemonNotFoundError:
        assert True


@responses.activate
def test_get_pokemon_not_found():
    responses.add(
        method=responses.GET,
        url=URL + 'test-pkm-fail',
        status=404
    )

    try:
        _ = get_pokemon('test-pkm-fail')
    except PokemonNotFoundError:
        assert True
