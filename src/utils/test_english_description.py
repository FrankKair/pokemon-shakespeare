from .english_description import get_english_description
from ..fixtures import pokemon_charizard, pokemon_charizard_without_description


def test_english_description_found():
    desc = get_english_description(pokemon_charizard)
    assert type(desc) == str
    assert len(desc) > 0


def test_english_description_not_found():
    try:
        _ = get_english_description(pokemon_charizard_without_description)
    except ValueError:
        assert True
