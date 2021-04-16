from dataclasses import dataclass
from typing import Dict, Any
from .error import TranslationNotFoundError


@dataclass(frozen=True)
class Success:
    total: int


@dataclass(frozen=True)
class Contents:
    translated: str
    text: str
    translation: str


@dataclass(frozen=True)
class Translation:
    success: Success
    contents: Contents


def decode(data: Dict[str, Any]) -> Translation:
    """ Maps the Shakespeare API call to a Translation object.

    Args:
        data: Dict[str, Any] representing the API response

    Returns:
        Translation object

    Raises:
        TranslationNotFoundError if data is empty or does not contain the necessary key/values
    """
    if not data:
        raise TranslationNotFoundError('No Shakespeare description found')

    try:
        return Translation(
            success=Success(total=data['success']['total']),
            contents=Contents(
                translated=data['contents']['translated'],
                text=data['contents']['text'],
                translation=data['contents']['translation']
            )
        )
    except KeyError:
        raise TranslationNotFoundError('No Shakespeare description found')
