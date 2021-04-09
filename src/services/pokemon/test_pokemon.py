import responses
from .models import decode
from .client import get_pokemon
from .fixtures import species_charizard, pokemon_charizard


URL = 'https://pokeapi.co/api/v2/pokemon-species/'


def test_pokemon_decoder():
    result = decode(species_charizard)
    assert result == pokemon_charizard


def test_pokemon_decoder_fail_empty():
    try:
        _ = decode({})
    except ValueError:
        assert True


def test_pokemon_decoder_fail_bad_json():
    try:
        _ = decode({'data': 'hello', 'data2': 'hello2'})
    except ValueError:
        assert True


@responses.activate
def test_pokemon_cached():
    responses.add(
        method=responses.GET,
        url=URL + 'charizard',
        json=species_charizard,
        status=200
    )

    p = get_pokemon('charizard')
    p = get_pokemon('charizard')

    info = get_pokemon.cache_info()
    assert info.hits == 1
    assert info.misses == 1
    assert info.maxsize == 16
    assert info.currsize == 1


@responses.activate
def test_get_pokemon_not_found():
    responses.add(
        method=responses.GET,
        url=URL + 'test-pkm-fail',
        status=404
    )

    try:
        _ = get_pokemon('test-pkm-fail')
    except ValueError:
        assert True
