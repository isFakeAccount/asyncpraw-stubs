"""Provide the MessageableMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from asyncpraw.util.deprecated_args import _deprecate_args

if TYPE_CHECKING:
    import asyncpraw

class MessageableMixin:
    @_deprecate_args("subject", "message", "from_subreddit")
    async def message(
        self,
        *,
        from_subreddit: asyncpraw.models.Subreddit | str | None = None,
        message: str,
        subject: str,
    ) -> None: ...
