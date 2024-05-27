from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from tasty_api.recipe import Completion, Recipe


@dataclass(frozen=True, slots=True)
class CompletionData:
    """Custom class to destructure auto complete requests."""

    results: list[Completion]

    @classmethod
    def from_dict(cls, data: dict[str, list[dict[str, str]]]) -> CompletionData:
        return CompletionData(
            [Completion.from_dict(result) for result in data["results"]]
        )


@dataclass(frozen=True, slots=True)
class RecipeListData:
    """Custom class to destructure recipes/list requests."""

    count: int
    results: list[Recipe]

    # TODO (maybe): Replace the Any with the full type of the dictionary. Big maybe.
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RecipeListData:
        return RecipeListData(
            data["count"], [Recipe.from_dict(result) for result in data["results"]]
        )
