from functools import lru_cache
import requests
from .models import Translation, decode


BASE_ENDPOINT = "https://api.funtranslations.com/translate/"
SHAKESPEARE_ENDPOINT = BASE_ENDPOINT + "shakespeare.json"


@lru_cache(maxsize=16)
def get_translation(desc: str) -> str:
    response = requests.post(url=SHAKESPEARE_ENDPOINT, data={'text': desc})
    if response.status_code == 429:
        raise requests.exceptions.HTTPError('Too many requests')

    data = response.json()
    translation = decode(data)
    return translation.contents.translated
