from dataclasses import dataclass
from typing import Iterator

from prawler.client import RedditPrawClient
from prawler.model import Redditor


@dataclass(frozen=True)
class RedditorProfileConfig:
    usernames: list[str]


class RedditorCrawler:
    def __init__(self, client: RedditPrawClient) -> None:
        self._client = client

    def from_usernames(self, cfg: RedditorProfileConfig) -> Iterator[Redditor]:
        for username in cfg.usernames:
            try:
                redditor = self._client.redditor(username)
                yield Redditor.from_praw(redditor)
            except Exception:  # noqa: BLE001
                pass
