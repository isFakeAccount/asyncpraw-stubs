from __future__ import annotations

from typing import TYPE_CHECKING, Any, NoReturn

from .exceptions import RedditAPIException

if TYPE_CHECKING:
    import asyncpraw

    from .models.reddit.base import RedditBase

class Objector:
    @classmethod
    def check_error(cls, data: list[Any] | dict[str, dict[str, str]]) -> NoReturn: ...
    @classmethod
    def parse_error(cls, data: list[Any] | dict[str, dict[str, str]]) -> RedditAPIException | None: ...
    def __init__(self, reddit: asyncpraw.Reddit, parsers: dict[str, Any] | None = None) -> None: ...
    def objectify(self, data: dict[str, Any] | list[Any] | bool | None) -> RedditBase | dict[str, Any] | list[Any] | bool | None: ...
