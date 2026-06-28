from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone

from praw.models import Redditor as PrawRedditor


@dataclass(frozen=True)
class Redditor:
    # Identity
    name: str
    id: str

    # Karma
    link_karma: int
    comment_karma: int

    # Metadata
    created_utc: datetime
    is_mod: bool
    is_gold: bool
    has_verified_email: bool | None
    icon_img: str

    def to_dict(self, fields: list[str] | None = None) -> dict:
        data = asdict(self)
        data["created_utc"] = self.created_utc.isoformat()

        if fields:
            data = {k: data[k] for k in fields if k in data}

        return data

    @classmethod
    def from_praw(cls, redditor: PrawRedditor) -> "Redditor":
        return cls(
            name=redditor.name,
            id=redditor.id,
            link_karma=redditor.link_karma,
            comment_karma=redditor.comment_karma,
            created_utc=datetime.fromtimestamp(redditor.created_utc, tz=timezone.utc),
            is_mod=redditor.is_mod,
            is_gold=redditor.is_gold,
            has_verified_email=getattr(redditor, "has_verified_email", None),
            icon_img=getattr(redditor, "icon_img", ""),
        )

    @property
    def total_karma(self) -> int:
        return self.link_karma + self.comment_karma

    @property
    def age_days(self) -> float:
        delta = datetime.now(tz=timezone.utc) - self.created_utc

        return delta.total_seconds() / 86_400
