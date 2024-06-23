"""Provide the BaseList class."""

from __future__ import annotations

from typing import Any, ClassVar, Iterator, Optional

from asyncpraw.models.base import AsyncPRAWBase
from asyncpraw.reddit import Reddit

class BaseList(AsyncPRAWBase):
    """An abstract class to coerce a list into an :class:`.AsyncPRAWBase`."""

    CHILD_ATTRIBUTE: ClassVar[Optional[str]]

    def __contains__(self, item: Any) -> bool: ...
    def __getitem__(self, index: int) -> Any: ...
    def __init__(self, reddit: Reddit, _data: dict[str, Any]) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
