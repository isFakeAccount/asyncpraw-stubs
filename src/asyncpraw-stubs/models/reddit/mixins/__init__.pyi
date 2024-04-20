from typing import TYPE_CHECKING

from asyncpraw.models.reddit.mixins.editable import EditableMixin
from asyncpraw.models.reddit.mixins.fullname import FullnameMixin
from asyncpraw.models.reddit.mixins.gildable import GildableMixin
from asyncpraw.models.reddit.mixins.inboxable import InboxableMixin
from asyncpraw.models.reddit.mixins.inboxtoggleable import InboxToggleableMixin
from asyncpraw.models.reddit.mixins.messageable import MessageableMixin
from asyncpraw.models.reddit.mixins.modnote import ModNoteMixin
from asyncpraw.models.reddit.mixins.replyable import ReplyableMixin
from asyncpraw.models.reddit.mixins.reportable import ReportableMixin
from asyncpraw.models.reddit.mixins.savable import SavableMixin
from asyncpraw.models.reddit.mixins.votable import VotableMixin
from asyncpraw.util.deprecated_args import _deprecate_args

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw.models

__all__ = [
    "FullnameMixin",
    "EditableMixin",
    "FullnameMixin",
    "GildableMixin",
    "InboxableMixin",
    "InboxToggleableMixin",
    "MessageableMixin",
    "ModNoteMixin",
    "ReplyableMixin",
    "ReportableMixin",
    "SavableMixin",
    "VotableMixin",
]

class ThingModerationMixin(ModNoteMixin):
    async def _add_removal_reason(self, *, mod_note: str = "", reason_id: str | None = None) -> None: ...
    async def approve(self) -> None: ...
    @_deprecate_args("how", "sticky")
    async def distinguish(self, *, how: str = "yes", sticky: bool = False) -> None: ...
    async def ignore_reports(self) -> None: ...
    async def lock(self) -> None: ...
    @_deprecate_args("spam", "mod_note", "reason_id")
    async def remove(self, *, mod_note: str = "", spam: bool = False, reason_id: str | None = None) -> None: ...
    @_deprecate_args("message", "title", "type")
    async def send_removal_message(
        self,
        *,
        message: str,
        title: str = "ignored",
        type: str = "public",
    ) -> asyncpraw.models.Comment | None: ...
    async def undistinguish(self) -> None: ...
    async def unignore_reports(self) -> None: ...
    async def unlock(self) -> None: ...

class UserContentMixin(
    EditableMixin,
    GildableMixin,
    InboxToggleableMixin,
    ReplyableMixin,
    ReportableMixin,
    SavableMixin,
    VotableMixin,
): ...
