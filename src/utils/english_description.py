from ..services.pokemon import Pokemon


def get_english_description(pokemon: Pokemon) -> str:
    """ Given a Pokemon, retrieves its first English flavor_text_entry.

    Args:
        pokemon: Pokemon object

    Returns:
        string representing the English description

    Raises:
        ValueError if no description is found
    """
    for entry in pokemon.flavor_text_entries:
        if entry.language.name == 'en':
            return entry.flavor_text

    raise ValueError(f"No English description found for {pokemon.name}")
