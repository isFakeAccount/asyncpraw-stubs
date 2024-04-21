"""Provide the Reddit class."""

from __future__ import annotations

import re
from typing import IO, TYPE_CHECKING, Any, AnyStr, AsyncGenerator, Iterable, TypedDict

import asyncprawcore.auth
from asyncpraw import models
from asyncpraw.exceptions import (
    RedditAPIException,
)
from asyncpraw.models.util import deprecate_lazy
from asyncpraw.util.deprecated_args import _deprecate_args
from asyncprawcore.requestor import Requestor
from typing_extensions import NotRequired, Unpack

if TYPE_CHECKING:
    import asyncpraw
    import asyncpraw.models
    import asyncprawcore

    from .util.token_manager import BaseTokenManager

Comment = models.Comment
Redditor = models.Redditor
Submission = models.Submission
Subreddit = models.Subreddit

class ConfigSettings(TypedDict):
    """Represents a configuration options that can be passed through initializer of the Reddit class."""

    client_id: str
    """The OAuth client ID associated with your registered Reddit application."""
    client_secret: NotRequired[str | None]
    """The OAuth client secret associated with your registered Reddit application. This option is required for all application types, however, the value must 
    be set to `None` for installed applications."""
    user_agent: str
    """A unique description of your application. The following format is recommended `<platform>:<app ID>:<version string> (by u/<reddit username>)`"""

    check_for_updates: NotRequired[bool]
    """Check for new versions of Async PRAW and print to stdout if newer version is available (default: `True`)."""
    comment_kind: NotRequired[str]
    """The type prefix for comments on the `Reddit` instance (default: `t1`_)."""
    message_kind: NotRequired[str]
    """The type prefix for messages on the `Reddit` instance (default: `t4`_)."""
    oauth_url: NotRequired[str]
    """The URL used to access the `Reddit` instance's API (default: `https://oauth.reddit.com`)."""
    password: NotRequired[str]
    """The password of the Reddit account associated with your registered Reddit script application."""
    ratelimit_seconds: NotRequired[int]
    """Controls the maximum number of seconds Async PRAW will capture ratelimits returned in JSON data (default: `5`)."""
    reddit_url: NotRequired[str]
    """The URL used to access the `Reddit` instance. Async PRAW assumes the endpoints for establishing OAuth authorization are accessible under this URL 
    (default: `https://www.reddit.com`)."""
    redditor_kind: NotRequired[str]
    """The type prefix for redditors on the `Reddit` instance (default: `t2`_)."""
    redirect_uri: NotRequired[str]
    """The redirect URI associated with your registered Reddit application. This field is unused for script applications and is only needed for both 
    web applications, and installed applications when the `url()` method is used."""
    refresh_token: NotRequired[str]
    """Lets you use `refresh_token` for authorization. Used in web applications and installed applications where `refresh_token` maybe saved."""
    short_url: NotRequired[str]
    """The URL used to generate short links on the `Reddit instance (default: `https://redd.it`)"""
    submission_kind: NotRequired[str]
    """The type prefix for subissions on the `Reddit` instance (default: `t3`_)."""
    subreddit_kind: NotRequired[str]
    """The type prefix for subreddits on the `Reddit` instance (default: `t5`_)."""
    timeout: NotRequired[int]
    """Controls the amount of time Async PRAW will wait for a request from Reddit to complete before throwing an exception (default: `16`)."""
    username: NotRequired[str]
    """The username of the Reddit account associated with your registered Reddit script application."""
    warn_comment_sort: NotRequired[bool]
    """Log a warning when `comment_sort` attribute of a submission is updated after `_fetch()` has been called (default: true)."""

class Reddit:
    update_checked: bool
    _ratelimit_regex: re.Pattern[str]

    @property
    def _next_unique(self) -> int: ...
    @property
    def read_only(self) -> bool: ...
    @read_only.setter
    def read_only(self, value: bool) -> None: ...
    @property
    def validate_on_submit(self) -> bool: ...
    @validate_on_submit.setter
    def validate_on_submit(self, val: bool) -> None: ...
    async def __aenter__(self) -> Reddit: ...
    async def __aexit__(self, exc_type: type | None, exc: BaseException | None, traceback: Any | None) -> None: ...
    def __deepcopy__(self, memodict: dict[str, Any] | None = None) -> Reddit: ...
    def __enter__(self) -> Reddit: ...
    def __exit__(self, *_args: object) -> None: ...
    def __init__(
        self,
        site_name: str | None = None,
        *,
        config_interpolation: str | None = None,
        requestor_class: type[Requestor] | None = None,
        requestor_kwargs: dict[str, Any] | None = None,
        token_manager: BaseTokenManager | None = None,
        **config_settings: Unpack[ConfigSettings],
    ) -> None: ...
    def _check_for_update(self) -> None: ...
    def _handle_rate_limit(self, exception: RedditAPIException) -> int | float | None: ...
    async def _objectify_request(
        self,
        *,
        data: dict[str, str | Any] | bytes | IO | str | None = None,  # type: ignore
        files: dict[str, IO] | None = None,  # type: ignore
        json: dict[Any, Any] | list[Any] | None = None,
        method: str = "",
        params: str | dict[str, str] | None = None,
        path: str = "",
    ) -> Any: ...
    def _prepare_asyncprawcore(
        self,
        *,
        requestor_class: type[Requestor] | None = None,
        requestor_kwargs: Any | None = None,
    ) -> Requestor: ...
    def _prepare_common_authorizer(self, authenticator: asyncprawcore.auth.BaseAuthenticator) -> None: ...
    def _prepare_objector(self) -> None: ...
    def _prepare_trusted_asyncprawcore(self, requestor: Requestor) -> None: ...
    def _prepare_untrusted_asyncprawcore(self, requestor: Requestor) -> None: ...
    async def close(self) -> None: ...
    async def _resolve_share_url(self, url: str) -> str: ...
    @_deprecate_args("id", "url", "fetch")
    @deprecate_lazy
    async def comment(
        self,
        id: str | None = None,
        *,
        fetch: bool = True,
        url: str | None = None,
        **_: Any,
    ) -> models.Comment: ...
    @_deprecate_args("path", "data", "json", "params")
    async def delete(
        self,
        path: str,
        *,
        data: dict[str, str | Any] | bytes | IO | str | None = None,  # type: ignore
        json: dict[Any, Any] | list[Any] | None = None,
        params: str | dict[str, str] | None = None,
    ) -> Any: ...
    def domain(self, domain: str) -> models.DomainListing: ...
    @_deprecate_args("path", "params")
    async def get(
        self,
        path: str,
        *,
        params: str | dict[str, str | int] | None = None,
    ) -> Any: ...
    @_deprecate_args("fullnames", "url", "subreddits")
    def info(
        self,
        *,
        fullnames: Iterable[str] | None = None,
        subreddits: Iterable[asyncpraw.models.Subreddit | str] | None = None,
        url: str | None = None,
    ) -> AsyncGenerator[asyncpraw.models.Subreddit | asyncpraw.models.Comment | asyncpraw.models.Submission, None,]: ...
    @_deprecate_args("path", "data", "json")
    async def patch(
        self,
        path: str,
        *,
        data: dict[str, str | Any] | bytes | IO[AnyStr] | str | None = None,
        json: dict[Any, Any] | list[Any] | None = None,
        params: str | dict[str, str] | None = None,
    ) -> Any: ...
    @_deprecate_args("path", "data", "files", "params", "json")
    async def post(
        self,
        path: str,
        *,
        data: dict[str, str | Any] | bytes | IO[AnyStr] | str | None = None,
        files: dict[str, IO[AnyStr]] | None = None,
        json: dict[Any, Any] | list[Any] | None = None,
        params: str | dict[str, str] | None = None,
    ) -> Any: ...
    @_deprecate_args("path", "data", "json")
    async def put(
        self,
        path: str,
        *,
        data: dict[str, str | Any] | bytes | IO[AnyStr] | str | None = None,
        json: dict[Any, Any] | list[Any] | None = None,
    ) -> Any: ...
    @_deprecate_args("nsfw")
    async def random_subreddit(self, *, nsfw: bool = False) -> asyncpraw.models.Subreddit: ...
    @_deprecate_args("name", "fullname", "fetch")
    async def redditor(
        self,
        name: str | None = None,
        *,
        fetch: bool = False,
        fullname: str | None = None,
    ) -> asyncpraw.models.Redditor: ...
    @_deprecate_args("method", "path", "params", "data", "files", "json")
    async def request(
        self,
        *,
        data: dict[str, str | Any] | bytes | IO[AnyStr] | str | None = None,
        files: dict[str, IO[AnyStr]] | None = None,
        json: dict[Any, Any] | list[Any] | None = None,
        method: str,
        params: str | dict[str, str | int] | None = None,
        path: str,
    ) -> Any: ...
    @_deprecate_args("id", "url", "fetch")
    @deprecate_lazy
    async def submission(
        self,
        id: str | None = None,
        *,
        fetch: bool = True,
        url: str | None = None,
        **_: Any,
    ) -> asyncpraw.models.Submission: ...
    async def username_available(self, name: str) -> bool: ...
