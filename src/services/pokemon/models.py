from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass(frozen=True)
class NameAndURL:
    name: str
    url: str


@dataclass(frozen=True)
class FlavorTextEntry:
    flavor_text: str
    language: NameAndURL
    version: NameAndURL


@dataclass(frozen=True)
class Pokemon:
    name: str
    flavor_text_entries: List[FlavorTextEntry]


def decode(data: Dict[str, Any]) -> Pokemon:
    pkm_name = data['name']
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

    return Pokemon(name=pkm_name, flavor_text_entries=entries)
