"""Provide the SubredditListingMixin class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator

from asyncpraw.models.base import AsyncPRAWBase
from asyncpraw.models.listing.mixins.base import BaseListingMixin
from asyncpraw.models.listing.mixins.gilded import GildedListingMixin
from asyncpraw.models.listing.mixins.rising import RisingListingMixin
from asyncpraw.util import cachedproperty

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw.models

class CommentHelper(AsyncPRAWBase):
    @property
    def _path(self) -> str: ...
    def __call__(self, **generator_kwargs: str | int | dict[str, str]) -> AsyncIterator[asyncpraw.models.Comment]: ...
    def __init__(self, subreddit: asyncpraw.models.Subreddit | SubredditListingMixin) -> None: ...

class SubredditListingMixin(BaseListingMixin, GildedListingMixin, RisingListingMixin):
    @cachedproperty
    def comments(self) -> CommentHelper: ...
    def __init__(self, reddit: asyncpraw.Reddit, _data: dict[str, Any] | None) -> None: ...
