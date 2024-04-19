"""Provide the EditableMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw.models

class EditableMixin:
    async def delete(self): ...
    async def edit(self, body: str) -> asyncpraw.models.Comment | asyncpraw.models.Submission: ...
