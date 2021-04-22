import responses
from requests.exceptions import HTTPError
from .models import decode
from .client import get_translation
from .error import TranslationNotFoundError
from ...fixtures import shakespeare_charizard, translation_charizard, description_charizard


URL = "https://api.funtranslations.com/translate/shakespeare.json"


def test_shakespeare_decoder():
    result = decode(shakespeare_charizard)
    assert result == translation_charizard


def test_shakespeare_decoder_fail_empty():
    try:
        _ = decode({})
    except TranslationNotFoundError:
        assert True


def test_shakespeare_decoder_fail_bad_json():
    try:
        _ = decode({'data': 'hello', 'data2': 'hello2'})
    except TranslationNotFoundError:
        assert True


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
