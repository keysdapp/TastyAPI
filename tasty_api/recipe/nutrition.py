from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class Nutrition:
    """Represents the nutrition facts of a recipe. All values are in grams."""

    calories: int
    carbohydrates: int
    fat: int
    fiber: int
    protein: int
    sugar: int
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Nutrition:
        return Nutrition(
            calories=data["calories"],
            carbohydrates=data["carbohydrates"],
            fat=data["fat"],
            fiber=data["fiber"],
            protein=data["protein"],
            sugar=data["sugar"],
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
