from fastapi import FastAPI, HTTPException, status
from requests.exceptions import HTTPError
from .utils import get_english_description, api_error
from .services.pokemon import get_pokemon, PokemonNotFoundError
from .services.shakespeare import get_translation, TranslationNotFoundError


app = FastAPI()


@app.get('/pokemon/{pokemon_name}')
async def pokemon_description(pokemon_name: str):
    """## Summary:
    Given a pokemon name, you get the pokemon description the way Shakespeare would have written it.

    Prepare the Pokedex and thy ole English lexicon 👒 🎩

    ## Args:
        pokemon_name: string

    ## Returns:
        { 'name': string, 'description': string }

    ## Errors:

        - 404: Pokemon does not exist
        - 404: Description not found
        - 422: Input is not a string
        - 429: Too many requests
    """
    try:
        pokemon = get_pokemon(pokemon_name)
        desc = get_english_description(pokemon)
        translation = get_translation(desc)
        return {'name': pokemon.name, 'description': translation}

    except PokemonNotFoundError as e:
        return api_error(status.HTTP_404_NOT_FOUND, e)

    except TranslationNotFoundError as e:
        return api_error(status.HTTP_404_NOT_FOUND, e)

    except HTTPError as e:
        return api_error(status.HTTP_429_TOO_MANY_REQUESTS, e)
