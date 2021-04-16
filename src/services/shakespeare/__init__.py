from .client import get_translation
from .models import Translation
from .error import TranslationNotFoundError
from .fixtures import description_charizard, shakespeare_charizard, translation_charizard

fixtures = {
    'description_charizard': description_charizard,
    'shakespeare_charizard': shakespeare_charizard,
    'translation_charizard': translation_charizard
}
