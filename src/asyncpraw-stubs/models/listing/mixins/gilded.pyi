"""Provide the GildedListingMixin class."""

from __future__ import annotations

from typing import Any, AsyncIterator

from asyncpraw.models.base import AsyncPRAWBase

class GildedListingMixin(AsyncPRAWBase):
    def gilded(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[Any]: ...
