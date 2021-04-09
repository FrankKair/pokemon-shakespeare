from functools import lru_cache
import requests
from .models import Translation, decode


BASE_ENDPOINT = "https://api.funtranslations.com/translate/"
SHAKESPEARE_ENDPOINT = BASE_ENDPOINT + "shakespeare.json"


@lru_cache(maxsize=16)
def get_translation(text: str) -> str:
    """ Given a str, returns a Shakespeare style translation.

    Args:
        text: The input string

    Returns:
        The translated string

    Raises:
        HTTPError (status 429) if too many requests are sent
    """
    response = requests.post(url=SHAKESPEARE_ENDPOINT, data={'text': text})
    if response.status_code == 429:
        raise requests.exceptions.HTTPError('Too many requests')

    data = response.json()
    translation = decode(data)
    return translation.contents.translated
