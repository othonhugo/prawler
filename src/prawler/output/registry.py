from __future__ import annotations

from prawler.output.base import Formatter
from .formatters import CsvFormatter, JsonFormatter, JsonLFormatter, MarkdownFormatter, TableFormatter

FORMATTERS: dict[str, type[Formatter]] = {
    "json": JsonFormatter,
    "jsonl": JsonLFormatter,
    "csv": CsvFormatter,
    "table": TableFormatter,
    "markdown": MarkdownFormatter,
}


def get_formatter(name: str) -> Formatter:
    cls = FORMATTERS.get(name)

    if cls is None:
        valid = ", ".join(FORMATTERS)
        raise SystemExit(f"Unknown format '{name}'. Valid options: {valid}")

    return cls()
