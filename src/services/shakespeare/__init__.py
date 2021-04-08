from .client import get_translation
from .models import Translation


def fixtures():
    from .fixtures import description_charizard, shakespeare_charizard, translation_charizard
    return {
        'description_charizard': description_charizard,
        'shakespeare_charizard': shakespeare_charizard,
        'translation_charizard': translation_charizard
    }
