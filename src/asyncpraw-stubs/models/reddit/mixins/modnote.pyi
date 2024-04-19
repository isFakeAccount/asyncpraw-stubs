"""Provide the ModNoteMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncGenerator

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw.models

class ModNoteMixin:
    def author_notes(self, **generator_kwargs: Any) -> AsyncGenerator[asyncpraw.models.ModNote, None]: ...
    async def create_note(self, *, label: str | None = None, note: str, **other_settings: Any) -> asyncpraw.models.ModNote: ...
