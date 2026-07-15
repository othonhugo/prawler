from __future__ import annotations

import itertools
import sys

import typer

from prawler.cli.options import FieldsOption, FileFormatOption, FilePathArg, FilterOption, FormatOption, LimitOption, OutputOption
from prawler.output import OutputFormat, get_formatter, make_sink
from prawler.pipeline import build_pipeline, make_field_select_stage, make_filter_stage
from prawler.reader import FileReader


def input(
    file: FilePathArg,
    input_format: FileFormatOption = None,
    format: FormatOption = OutputFormat.JSONL,
    output: OutputOption = "-",
    fields: FieldsOption = None,
    filter: FilterOption = None,
    limit: LimitOption = None,
) -> None:
    """Process a local file through the pipeline. No API requests made.

    Accepts JSONL, JSON array, or CSV files produced by any previous crawl.
    Use '-' as FILE to read from stdin.

    Examples:

    \b
      # Re-filter a saved dataset and convert to CSV
      praw-cli input posts.jsonl --filter "score>=500" --format csv

      # Transform JSONL to a markdown table preview
      praw-cli input posts.jsonl --fields title,score,author --format markdown

      # Read from stdin
      cat posts.jsonl | praw-cli input -
    """

    reader = FileReader()

    try:
        raw_stream = reader.read(file, input_format)
    except FileNotFoundError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=1) from exc
    except ValueError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=1) from exc

    # Apply limit before the pipeline so it short-circuits the source early
    if limit is not None:
        raw_stream = itertools.islice(raw_stream, limit)

    pipeline = build_pipeline(
        *[make_filter_stage(f) for f in (filter or [])],
        make_field_select_stage(fields.split(",") if fields else None),
    )

    make_sink(output).write(get_formatter(format).format(pipeline(raw_stream)))
