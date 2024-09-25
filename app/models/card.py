from enum import StrEnum

from pydantic import BaseModel, field_validator
from typing import List


class CardAttributeNames(StrEnum):
    COLOR = "color"
    SHAPE = "shape"
    NUMBER = "number"
    SHADING = "shading"


class Card(BaseModel):
    color: str
    shape: str
    number: int
    shading: str

    @field_validator("color", "shape", "shading")
    @classmethod
    def lowercase_strings(cls, value: str) -> str:
        if isinstance(value, str):
            return value.lower()
        return value

    def __getitem__(self, name: CardAttributeNames | str) -> str:
        if not hasattr(self, name):
            raise KeyError(
                f"Invalid attribute name: {name} in Card model. Valid attributes: color, shape, number, shading"
            )
        return getattr(self, name)


class CardSetRequest(BaseModel):
    cards: List[Card]
    set_size: int = 3


class CardSetResponse(BaseModel):
    sets: List[List[Card]]
