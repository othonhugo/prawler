from __future__ import annotations

from typing import Iterator, Protocol, runtime_checkable

Record = dict[str, object]


@runtime_checkable
class Formatter(Protocol):
    def format(self, items: Iterator[Record]) -> Iterator[str]: ...


@runtime_checkable
class Sink(Protocol):
    def write(self, chunks: Iterator[str]) -> None: ...
