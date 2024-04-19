"""Provide the ReportableMixin class."""
from __future__ import annotations

class ReportableMixin:
    async def report(self, reason: str) -> None: ...
