from fastapi.testclient import TestClient
import responses
from .app import app
from .fixtures import (
    species_charizard,
    shakespeare_charizard,
    translation_charizard
)


client = TestClient(app)


def test_input_is_not_string():
    try:
        _ = client.get('/pokemon/12')
    except:
        assert True


@responses.activate
def test_input_charizard():
    responses.add(
        method=responses.GET,
        url='https://pokeapi.co/api/v2/pokemon-species/charizard',
        json=species_charizard,
        status=200
    )

    responses.add(
        method=responses.POST,
        url="https://api.funtranslations.com/translate/shakespeare.json",
        json=shakespeare_charizard,
        status=200
    )

    mocked_response = {
        'name': 'charizard',
        'description': translation_charizard.contents.translated
    }

    response = client.get('/pokemon/charizard')
    data = response.json()
    assert data == mocked_response


@responses.activate
def test_input_unknown_pokemon():
    responses.add(
        method=responses.GET,
        url='https://pokeapi.co/api/v2/pokemon-species/testing',
        status=404
    )

    response = client.get('/pokemon/testing')
    assert response.status_code == 404
    assert response.json() == {'detail': 'testing not found'}
