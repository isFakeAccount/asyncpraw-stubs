"""Provide the DraftList class."""

from __future__ import annotations

from typing import ClassVar, Optional

from asyncpraw.models.list.base import BaseList

class DraftList(BaseList):
    CHILD_ATTRIBUTE: ClassVar[Optional[str]]
