from dataclasses import dataclass
from typing import Dict, Any


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
    t = Translation(
        success=Success(total=data['success']['total']),
        contents=Contents(
            translated=data['contents']['translated'],
            text=data['contents']['text'],
            translation=data['contents']['translation']
        )
    )
    return t
