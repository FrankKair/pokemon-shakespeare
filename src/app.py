from fastapi import FastAPI
from .pokemon_shakespeare_description import pokemon_shakespeare_description

app = FastAPI()


@app.get('/pokemon/{pokemon}')
def pkm_desc(pokemon: str):
    """## Summary:
    Given a pokemon name, you get the pokemon description the way Shakespeare would write it.

    Prepare the Pokedex and thy ole English lexicon 👒 🎩

    ## Args:
        pokemon: string

    ## Returns:
        { 'name': string, 'description': string }

    ## Errors:

    HTTP 400 BAD REQUEST if:

        - Pokemon does not exist
    """
    desc = pokemon_shakespeare_description(pokemon)
    return {'name': pokemon.lower(), 'description': desc}

