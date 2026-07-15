from __future__ import annotations

from enum import StrEnum

from prawler.output.base import Formatter
from .formatters import CsvFormatter, JsonFormatter, JsonLFormatter, MarkdownFormatter, TableFormatter


class OutputFormat(StrEnum):
    """All output formats supported by the formatter registry."""

    JSON = "json"
    JSONL = "jsonl"
    CSV = "csv"
    TABLE = "table"
    MARKDOWN = "markdown"


class FileFormat(StrEnum):
    """Subset of OutputFormat values that can be round-tripped as file inputs.

    ``table`` and ``markdown`` are output-only formats; they are not included
    here because they cannot be reliably parsed back into structured records.
    """

    JSONL = "jsonl"
    JSON = "json"
    CSV = "csv"


FORMATTERS: dict[OutputFormat, type[Formatter]] = {
    OutputFormat.JSON: JsonFormatter,
    OutputFormat.JSONL: JsonLFormatter,
    OutputFormat.CSV: CsvFormatter,
    OutputFormat.TABLE: TableFormatter,
    OutputFormat.MARKDOWN: MarkdownFormatter,
}


def get_formatter(name: OutputFormat | str) -> Formatter:
    try:
        key = OutputFormat(name)
    except ValueError:
        valid = ", ".join(OutputFormat)

        raise SystemExit(f"Unknown format '{name}'. Valid options: {valid}") from None

    return FORMATTERS[key]()
