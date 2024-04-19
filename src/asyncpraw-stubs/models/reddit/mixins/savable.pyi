"""Provide the SavableMixin class."""

from __future__ import annotations

from asyncpraw.util.deprecated_args import _deprecate_args

class SavableMixin:
    @_deprecate_args("category")
    async def save(self, *, category: str | None = None) -> None: ...
    async def unsave(self) -> None: ...
