from .english_description import get_english_description
from ..services.pokemon import fixtures


def test_english_description_found():
    p = fixtures['pokemon_charizard']
    desc = get_english_description(p)
    assert type(desc) == str
    assert len(desc) > 0


def test_english_description_not_found():
    p = fixtures['pokemon_charizard_without_description']
    try:
        _ = get_english_description(p)
    except ValueError:
        assert True
