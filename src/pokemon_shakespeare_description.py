from functools import lru_cache
from typing import Tuple
from .services.pokemon import get_pokemon 
from .services.shakespeare import get_translation


@lru_cache(maxsize=32)
def fancy_description(pkm_id: str) -> Tuple[str, str]:
    pokemon = get_pokemon(pkm_id)
    desc = ''
    for entry in pokemon.flavor_text_entries:
        if entry.language.name == 'en':
            desc = entry.flavor_text

    t = get_translation(desc)
    return pokemon.name, t.contents.translated
