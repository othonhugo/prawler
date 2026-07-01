from __future__ import annotations

import typer

from prawler.cli.options import FieldsOption, FormatOption, LimitOption, OutputOption, SortOption, SourceArg
from prawler.client import RedditPrawClient
from prawler.config import get_config
from prawler.crawler import CommentCrawler, SubmissionCommentConfig, UserCommentConfig
from prawler.output import get_formatter, make_sink

app = typer.Typer()


@app.command()
def comments(
    source: SourceArg,
    sort: SortOption = "new",
    limit: LimitOption = 100,
    format: FormatOption = "jsonl",
    output: OutputOption = "-",
    fields: FieldsOption = None,
) -> None:
    """Crawl comments from a submission (URL or ID) or a user (u/username)."""

    cfg = get_config()
    client = RedditPrawClient.from_config(cfg)
    crawler = CommentCrawler(client)

    field_list = fields.split(",") if fields else None

    if source.startswith("u/"):
        username = source.removeprefix("u/")
        stream = crawler.from_user(UserCommentConfig(username, sort, limit))
    elif source.startswith("http"):
        stream = crawler.from_submission(SubmissionCommentConfig(submission_url=source, limit=limit))
    else:
        stream = crawler.from_submission(SubmissionCommentConfig(submission_id=source, limit=limit))

    records = (comment.to_dict(field_list) for comment in stream)

    make_sink(output).write(get_formatter(format).format(records))
