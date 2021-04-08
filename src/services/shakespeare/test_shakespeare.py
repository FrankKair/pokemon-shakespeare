import responses
from requests.exceptions import HTTPError
from .models import decode
from .client import get_translation
from .fixtures import shakespeare_charizard, translation_charizard, description_charizard


URL = "https://api.funtranslations.com/translate/shakespeare.json"


def test_shakespeare_decoder():
    result = decode(shakespeare_charizard)
    assert result == translation_charizard


@responses.activate
def test_shakespeare_cached():
    responses.add(
        method=responses.POST,
        url=URL,
        json=shakespeare_charizard,
        status=200
    )

    t = get_translation(description_charizard)
    t = get_translation(description_charizard)

    info = get_translation.cache_info()
    assert info.hits == 1
    assert info.misses == 1
    assert info.maxsize == 16
    assert info.currsize == 1


@responses.activate
def test_correct_translation():
    responses.add(
        method=responses.POST,
        url=URL,
        json=shakespeare_charizard,
        status=200
    )

    t = get_translation(description_charizard)
    assert t == translation_charizard.contents.translated


@responses.activate
def test_too_many_requests():
    responses.add(
        method=responses.POST,
        url=URL,
        status=429
    )

    try:
        _ = get_translation(description_charizard)
    except HTTPError:
        assert True
