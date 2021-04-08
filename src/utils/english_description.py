from ..services.pokemon import Pokemon


def get_english_description(pokemon: Pokemon) -> str:
    for entry in pokemon.flavor_text_entries:
        if entry.language.name == 'en':
            return entry.flavor_text

    raise ValueError(f"No English description found for {pokemon.name}")
