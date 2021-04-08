from fastapi import FastAPI
from typing import Union
from .pokemon_shakespeare_description import fancy_description


app = FastAPI()


@app.get('/pokemon/{pokemon_name}')
def pokemon_description(pokemon_name: str):
    """## Summary:
    Given a pokemon name, you get the pokemon description the way Shakespeare would have written it.

    Prepare the Pokedex and thy ole English lexicon 👒 🎩

    ## Args:
        pokemon_name: string

    ## Returns:
        { 'name': string, 'description': string }

    ## Errors:

    HTTP 400 BAD REQUEST if:

        - Pokemon does not exist
    """
    breakpoint()
    import sys
    sys.exit(0)
    name, desc = fancy_description(pokemon_name)
    return {'name': name, 'description': desc}
