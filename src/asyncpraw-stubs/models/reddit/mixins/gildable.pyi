"""Provide the GildableMixin class."""

from typing import Any

from asyncpraw.util.deprecated_args import _deprecate_args

class GildableMixin:
    @_deprecate_args("gild_type", "is_anonymous", "message")
    async def award(
        self,
        *,
        gild_type: str = "gid_2",
        is_anonymous: bool = True,
        message: str | None = None,
    ) -> dict[Any, Any]: ...
    async def gild(self) -> dict[Any, Any]: ...
