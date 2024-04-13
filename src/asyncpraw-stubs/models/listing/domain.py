"""Provide the DomainListing class."""

from __future__ import annotations

from .mixins import BaseListingMixin, RisingListingMixin


class DomainListing(BaseListingMixin, RisingListingMixin):
    ...
