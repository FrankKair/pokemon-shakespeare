from functools import lru_cache
import requests
from .models import Translation, decode


BASE_ENDPOINT = "https://api.funtranslations.com/translate/"
SHAKESPEARE_ENDPOINT = BASE_ENDPOINT + "shakespeare.json"


@lru_cache(maxsize=32)
def get_translation(desc: str) -> Translation:
    response = requests.post(url=SHAKESPEARE_ENDPOINT, data={'text': desc})
    data = response.json()
    translation = decode(data)
    return translation
