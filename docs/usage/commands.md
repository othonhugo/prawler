# CLI Commands

The CLI is divided into four main commands, targeting different Reddit entities.

## Collect Posts (`posts`)

Extracts posts (submissions) from a specific subreddit.

- **Basic syntax:**

  ```bash
  praw-cli posts <subreddit_name>
  ```

  _(Optional: you can omit the `r/` prefix)_

- **Examples:**

  ```bash
  # Collect the top 100 "hot" posts (default) from r/python
  praw-cli posts python

  # Collect the top 500 most upvoted posts of all time from r/programming
  praw-cli posts programming --sort top --time all --limit 500
  ```

## Collect Comments (`comments`)

Extracts comments based on a post URL, post ID, or username.

- **Basic syntax:**

  ```bash
  praw-cli comments <URL | ID | u/username>
  ```

- **Examples:**

  ```bash
  # Collect comments using the post URL
  praw-cli comments https://reddit.com/r/python/comments/xyz123/example/

  # Collect comments by post ID
  praw-cli comments xyz123

  # Collect recent comments from a specific user
  praw-cli comments u/AutoModerator
  ```

## Search Posts (`search`)

Performs searches using Reddit's native search engine.

- **Basic syntax:**

  ```bash
  praw-cli search "your query"
  ```

- **Examples:**

  ```bash
  # Search for "machine learning" across all of Reddit
  praw-cli search "machine learning"

  # Search only within the r/dataengineering subreddit
  praw-cli search "pipeline" --sub dataengineering

  # Sort search results by number of comments
  praw-cli search "python" --sort comments
  ```

## User Data (`user`)

Focuses on extracting data related to a user profile (Redditor).

- **Basic syntax:**

  ```bash
  praw-cli user <username> --mode <posts | comments | profile>
  ```

- **Examples:**

  ```bash
  # Return user profile metadata
  praw-cli user spez --mode profile

  # Return recent posts made by the user
  praw-cli user spez --mode posts

  # Return recent comments made by the user
  praw-cli user spez --mode comments
  ```
