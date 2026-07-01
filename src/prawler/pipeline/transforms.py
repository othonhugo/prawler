from __future__ import annotations

from collections.abc import Iterator

from prawler.pipeline.stage import PipelineStage, Record


def make_field_select_stage(fields: list[str] | None) -> PipelineStage:
    if not fields:
        return lambda stream: stream

    def stage(stream: Iterator[Record]) -> Iterator[Record]:
        return ({k: record[k] for k in fields if k in record} for record in stream)

    return stage
