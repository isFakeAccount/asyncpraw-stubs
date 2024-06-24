"""Provide the SubmissionListingMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING, AsyncIterator

from asyncpraw.models.base import AsyncPRAWBase

if TYPE_CHECKING:
    import asyncpraw.models

class SubmissionListingMixin(AsyncPRAWBase):
    def duplicates(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[asyncpraw.models.Submission]: ...
