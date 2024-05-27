from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .ingredient import Ingredient
from .measurement import Measurement


@dataclass(frozen=True, slots=True)
class Component:
    """
    Collection of details surrounding an ingredient.
    Ex: 10 cloves peeled garlic
    """

    extra_comment: str
    id: int
    ingredient: Ingredient
    measurements: list[Measurement]
    position: int
    raw_text: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Component:
        return Component(
            extra_comment=data["extra_comment"],
            id=data["id"],
            ingredient=Ingredient.from_dict(data["ingredient"]),
            measurements=[
                Measurement.from_dict(measurement)
                for measurement in data["measurements"]
            ],
            position=data["position"],
            raw_text=data["raw_text"],
        )
