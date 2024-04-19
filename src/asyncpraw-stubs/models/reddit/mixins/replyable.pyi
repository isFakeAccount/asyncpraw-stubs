"""Provide the ReplyableMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import asyncpraw.models

class ReplyableMixin:
    async def reply(self, body: str) -> asyncpraw.models.Comment | asyncpraw.models.Message | None: ...
