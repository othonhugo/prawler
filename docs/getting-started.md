# Getting Started

Welcome to praw-cli! This guide will help you install the tool, set up your Reddit API credentials, and run your first extraction.

## Installation

### Option 1: Via PyPI (Recommended)

You can install the stable package directly using `pip` or `pipx`:

```bash
pip install praw-cli
```

Once installed, the `praw-cli` command will be available globally in your environment.

### Option 2: From Source (Using `uv`)

If you want to contribute to development or run the codebase locally:

```bash
# 1. Enter the project directory
cd praw-cli

# 2. Install dependencies and the current package into the virtual environment
uv sync

# 3. Activate the newly created virtual environment
source .venv/bin/activate

# 4. The `praw-cli` command is now available in your terminal!
praw-cli --help
```

## Authentication (Environment Variables)

To use praw-cli, you must authenticate with the Reddit API. We use environment variables to ensure your credentials are never saved in your terminal history or accidentally committed to source control.

The following variables are supported:

| Variable                | Description                                     | Required                     |
| ----------------------- | ----------------------------------------------- | ---------------------------- |
| `PRAWLER_CLIENT_ID`     | Your Reddit application Client ID.              | **Yes**                      |
| `PRAWLER_CLIENT_SECRET` | Your Reddit application Client Secret.          | **Yes**                      |
| `PRAWLER_USER_AGENT`    | A descriptive name for your bot.                | No (Default: `praw-cli/0.2`) |
| `PRAWLER_USERNAME`      | Your Reddit username (for user-scoped actions). | No                           |
| `PRAWLER_PASSWORD`      | Your Reddit password (for user-scoped actions). | No                           |

**Quick usage example:**

```bash
export PRAWLER_CLIENT_ID="your_client_id_here"
export PRAWLER_CLIENT_SECRET="your_client_secret_here"

# Test your authentication by fetching posts:
praw-cli posts python
```

You can also add these variables to a local `.env` file if your environment loads variables automatically, or pass them inline:

```bash
PRAWLER_CLIENT_ID="id" PRAWLER_CLIENT_SECRET="secret" praw-cli search "API"
```

## Next Steps

Now that you have praw-cli installed and authenticated, check out the core CLI commands:

- [CLI Commands Guide](usage/commands.md)
- [Pipelines & Filtering](usage/pipelines-filters.md)
