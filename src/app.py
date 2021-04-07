from fastapi import FastAPI
from typing import Union
from .pokemon_shakespeare_description import fancy_description


app = FastAPI()


@app.get('/pokemon/{pokemon_id}')
def pokemon_description(pokemon_id: Union[str, int]):
    """## Summary:
    Given a pokemon name, you get the pokemon description the way Shakespeare would have written it.

    Prepare the Pokedex and thy ole English lexicon 👒 🎩

    ## Args:
        pokemon_id: string or integer representing a pokemon

    ## Returns:
        { 'name': string, 'description': string }

    ## Errors:

    HTTP 400 BAD REQUEST if:

        - Pokemon does not exist
    """
    name, desc = fancy_description(pokemon_id)
    return {'name': name, 'description': desc}
