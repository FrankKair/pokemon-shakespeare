from fastapi import FastAPI, HTTPException, status
from requests.exceptions import HTTPError
from .utils import get_english_description
from .services.pokemon import get_pokemon
from .services.shakespeare import get_translation


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

        - 400: Pokemon does not exist
        - 400: Description not found
        - 422: Input is not a string
        - 429: Too many requests
    """
    try:
        pokemon = get_pokemon(pokemon_name)
        desc = get_english_description(pokemon)
        translation = get_translation(desc)
        return {'name': pokemon.name, 'description': translation}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except HTTPError as e:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=str(e))
