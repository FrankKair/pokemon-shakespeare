from dataclasses import dataclass
from typing import Dict
from functools import lru_cache
import requests


#@dataclass(frozen=True)
#class Success:
#    total: int
#
#
#@dataclass(frozen=True)
#class Contents:
#    translated: str
#    text: str
#    translation: str


@dataclass(frozen=True)
class Translation:
    success: Dict[str, int]
    contents: Dict[str, str]


@lru_cache(maxsize=32)
def shakespeare_translation(desc: str) -> str:
    ENDPOINT = "https://api.funtranslations.com/translate/shakespeare.json"
    data = requests.post(url=ENDPOINT, data={'text': desc}).json()
    return Translation(**data).contents['translated']

