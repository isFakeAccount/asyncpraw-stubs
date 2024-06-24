"""Provide the RisingListingMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator

from asyncpraw.models.base import AsyncPRAWBase

if TYPE_CHECKING:
    import asyncpraw.models

class RisingListingMixin(AsyncPRAWBase):
    def random_rising(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[asyncpraw.models.Submission]: ...
    def rising(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[asyncpraw.models.Submission]: ...
