"""Provide the TrophyList class."""

from __future__ import annotations

from typing import ClassVar, Optional

from asyncpraw.models.list.base import BaseList

class TrophyList(BaseList):
    CHILD_ATTRIBUTE: ClassVar[Optional[str]]
