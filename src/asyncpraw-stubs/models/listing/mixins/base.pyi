"""Provide the BaseListingMixin class."""

from __future__ import annotations

from typing import Any, AsyncIterator, ClassVar

from asyncpraw.models.base import AsyncPRAWBase
from asyncpraw.util import _deprecate_args

class BaseListingMixin(AsyncPRAWBase):
    VALID_TIME_FILTERS: ClassVar[set[str]]

    @staticmethod
    def _validate_time_filter(time_filter: str) -> None: ...
    def _prepare(self, *, arguments: dict[str, Any], sort: str) -> str: ...
    @_deprecate_args("time_filter")
    def controversial(
        self,
        *,
        time_filter: str = "all",
        **generator_kwargs: str | int | dict[str, str],
    ) -> AsyncIterator[Any]: ...
    def hot(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[Any]: ...
    def new(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[Any]: ...
    @_deprecate_args("time_filter")
    def top(
        self,
        *,
        time_filter: str = "all",
        **generator_kwargs: str | int | dict[str, str],
    ) -> AsyncIterator[Any]: ...
