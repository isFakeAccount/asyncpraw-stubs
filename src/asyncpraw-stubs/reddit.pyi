from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, TypedDict

from typing_extensions import NotRequired, Unpack

if TYPE_CHECKING:
    import asyncprawcore

    from .util.token_manager import BaseTokenManager

class ConfigSettings(TypedDict):
    client_id: str
    client_secret: str
    user_agent: str
    
    check_for_updates: NotRequired[bool]
    comment_kind: NotRequired[str]
    message_kind: NotRequired[str]
    oauth_url: NotRequired[str]
    password: NotRequired[str]
    ratelimit_seconds: NotRequired[int]
    reddit_url: NotRequired[str]
    redditor_kind: NotRequired[str]
    redirect_uri: NotRequired[str]
    refresh_token: NotRequired[str]
    short_url: NotRequired[str]
    submission_kind: NotRequired[str]
    subreddit_kind: NotRequired[str]
    timeout: NotRequired[int]
    username: NotRequired[str]
    warn_comment_sort: NotRequired[bool]


class Reddit:
    update_checked: bool
    _ratelimit_regex: re.Pattern

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
        requestor_class: type[asyncprawcore.requestor.Requestor] | None = None,
        requestor_kwargs: dict[str, Any] | None = None,
        token_manager: BaseTokenManager | None = None,
        **config_settings: Unpack[ConfigSettings],
    ) -> None: ...
