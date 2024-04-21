"""Provide helper classes used by other models."""

from __future__ import annotations

from typing import Callable, TypeVar

from typing_extensions import ParamSpec

Param = ParamSpec("Param")
RetType = TypeVar("RetType")

def deprecate_lazy(func: Callable[Param, RetType]) -> Callable[Param, RetType]: ...
