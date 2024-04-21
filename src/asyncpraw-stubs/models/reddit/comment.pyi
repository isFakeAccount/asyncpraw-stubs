"""Provide the Comment class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from asyncpraw.models.comment_forest import CommentForest
from asyncpraw.models.reddit.base import RedditBase
from asyncpraw.models.reddit.mixins import FullnameMixin, InboxableMixin, ThingModerationMixin, UserContentMixin
from asyncpraw.util.cache import cachedproperty

if TYPE_CHECKING:  # pragma: no cover
    from asyncpraw import Reddit
    from asyncpraw.models import Redditor, Submission, Subreddit

class Comment(InboxableMixin, UserContentMixin, FullnameMixin, RedditBase):
    author: Redditor
    body_html: str
    body: str
    created_utc: float
    distinguished: bool
    edited: bool
    id: str
    is_submitter: bool
    link_id: str
    parent_id: str
    permalink: str
    saved: bool
    score: int
    stickied: bool
    subreddit_id: str
    subreddit: Subreddit

    @staticmethod
    def id_from_url(url: str) -> str: ...
    @cachedproperty
    def mod(self) -> CommentModeration: ...
    @property
    def _kind(self) -> str: ...
    @property
    def is_root(self) -> bool: ...
    @property
    def replies(self) -> CommentForest: ...
    @property
    def submission(self) -> Submission: ...
    @submission.setter
    def submission(self, submission: Submission) -> None: ...
    def __init__(
        self,
        reddit: Reddit,
        id: str | None = None,
        url: str | None = None,
        _data: dict[str, Any] | None = None,
    ) -> None: ...
    def __setattr__(
        self,
        attribute: str,
        value: str | Redditor | CommentForest | Subreddit,
    ) -> None: ...
    def _extract_submission_id(self) -> str: ...
    async def _fetch(self) -> None: ...
    def _fetch_info(self) -> tuple[Literal["info"], dict[str, Any], dict[str, str]]: ...
    async def parent(
        self,
    ) -> Comment | Submission: ...
    async def refresh(self) -> Comment: ...

class CommentModeration(ThingModerationMixin): ...
