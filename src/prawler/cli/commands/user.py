from __future__ import annotations

import typer

from prawler.cli.options import FieldsOption, FormatOption, LimitOption, OutputOption, SortOption, UserMode, UserModeOption, UsernameArg
from prawler.client import RedditPrawClient
from prawler.config import get_config
from prawler.crawler import CommentCrawler, PostCrawler, RedditorCrawler, RedditorProfileConfig, SubredditSort, UserCommentConfig, UserCrawlConfig
from prawler.output import get_formatter, make_sink

app = typer.Typer()


@app.command()
def user(
    username: UsernameArg,
    mode: UserModeOption = UserMode.POSTS,
    sort: SortOption = "new",
    limit: LimitOption = 100,
    format: FormatOption = "jsonl",
    output: OutputOption = "-",
    fields: FieldsOption = None,
) -> None:
    """Crawl a Redditor's posts, comments, or profile."""

    cfg = get_config()
    client = RedditPrawClient.from_config(cfg)

    field_list = fields.split(",") if fields else None

    match mode:
        case UserMode.POSTS:
            post_stream = PostCrawler(client).from_user(UserCrawlConfig(username, SubredditSort(sort), limit))
            records = (post.to_dict(field_list) for post in post_stream)

        case UserMode.COMMENTS:
            comment_stream = CommentCrawler(client).from_user(UserCommentConfig(username, sort, limit))
            records = (comment.to_dict(field_list) for comment in comment_stream)

        case UserMode.PROFILE:
            redditor_stream = RedditorCrawler(client).from_usernames(RedditorProfileConfig([username]))
            records = (redditor.to_dict(field_list) for redditor in redditor_stream)

    make_sink(output).write(get_formatter(format).format(records))
