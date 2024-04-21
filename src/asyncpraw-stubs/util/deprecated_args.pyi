"""Positional argument deprecation decorator."""

from __future__ import annotations

from typing import Callable, TypeVar

from typing_extensions import ParamSpec

PT = ParamSpec("PT")
RT = TypeVar("RT")

def _deprecate_args(
    *old_args: str,
) -> Callable[[Callable[PT, RT]], Callable[PT, RT]]: ...
