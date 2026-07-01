from __future__ import annotations

from collections.abc import Callable, Iterator
from functools import reduce

Record = dict[str, object]
PipelineStage = Callable[[Iterator[Record]], Iterator[Record]]


def build_pipeline(*stages: PipelineStage) -> PipelineStage:
    if not stages:
        return lambda stream: stream

    return reduce(lambda f, g: lambda stream: g(f(stream)), stages)
