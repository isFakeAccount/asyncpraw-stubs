"""Provide helper classes used by other models."""

from __future__ import annotations

from typing import Any, Callable

def deprecate_lazy(func: Callable[..., Any]) -> Callable[..., Any]: ...
