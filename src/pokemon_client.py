from dataclasses import dataclass
from typing import Dict, List
from functools import lru_cache
import requests


@dataclass(frozen=True)
class NameAndURL:
    name: str
    url: str


@dataclass(frozen=True)
class FlavorTextEntry:
    flavor_text: str
    language: NameAndURL
    version: NameAndURL


@lru_cache(maxsize=32)
def pokemon_flavor_text_entries(pkm_name: str) -> List[FlavorTextEntry]:
    ENDPOINT = 'https://pokeapi.co/api/v2/pokemon-species/'
    url = ENDPOINT + pkm_name
    data = requests.get(url).json()
    flavor_text_entries = data['flavor_text_entries']

    entries = []
    for entry in flavor_text_entries:
        language = NameAndURL(
                name=entry['language']['name'],
                url=entry['language']['url'])

        version = NameAndURL(
                name=entry['version']['name'],
                url=entry['version']['url'])

        entries.append(
            FlavorTextEntry(
                flavor_text=entry['flavor_text'],
                language=language,
                version=version
            )
        )

    return entries


def english_description_ruby_version(entries: List[FlavorTextEntry]) -> str:
    for entry in entries:
        if entry.language.name == 'en' and entry.version.name == 'ruby':
            return entry.flavor_text


def pokemon_description(name: str) -> str:
    entries = pokemon_flavor_text_entries(name)
    return english_description_ruby_version(entries)

