"""Positional argument deprecation decorator."""
from __future__ import annotations

from typing import Any, Callable

def _deprecate_args(*old_args: str) -> Callable[..., Any]: ...
