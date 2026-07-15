# praw-cli

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-purple.svg)](https://github.com/astral-sh/ruff)

A composable Reddit crawler for the command line. Fetch posts and comments from any source, shape the data through a lazy filter pipeline, and emit it in any format — all without writing a single line of Python.

```bash
# stream the top 500 posts from r/MachineLearning as JSONL
praw-cli posts r/MachineLearning --sort top --time year --limit 500 --format jsonl

# search across r/programming, keep only high-signal posts, project to four fields
praw-cli search "New web framework" --sub r/programming \
  --filter "score>=100" --filter "num_comments>=10" \
  --fields id,title,score,url --format csv --output results.csv

# full comment tree of a submission, depth-first, minimum score 5
praw-cli comments https://reddit.com/r/Python/comments/xyz/ \
  --depth 10 --min-score 5 --format jsonl

# fetch a user's recent posts as a terminal table
praw-cli user spez --mode posts --limit 20 --format table

# re-process a saved dataset offline — no API, no credentials needed
praw-cli input posts.jsonl --filter "score>=500" --format csv --output filtered.csv
```

## Key Features & How They Solve Your Problems

### Smart Memory & Reliability

- **Constant Memory Footprint (Lazy Pipelines)**: Typical scrapers buffer huge arrays in memory, causing out-of-memory crashes on large crawls. praw-cli processes data lazily item-by-item (`Iterator[Record]`). Streaming 100,000 posts uses the same constant memory as streaming 10.
- **Resumable Extractions (Checkpointing)**: Long-running scrapes often fail halfway due to network drops or API limits. praw-cli checkpoints progress, letting you `--resume` interrupted sessions without refetching from scratch.
- **Offline Re-processing (`input`)**: Apply new filters, change output formats, or extract field subsets from any previously saved `.jsonl`, `.json`, or `.csv` file — without touching the API or needing credentials. Pipe from stdin too.

### Zero-Code Data Preparation

- **Data Science-Focused DSL**: Stop writing custom Python scripts just to filter text. Chain `--filter` conditions directly in the CLI:
  - _NLP Cleaning_: Keep long-form content using `selftext len>= 500`.
  - _Temporal Sorting_: Restrict dates natively using ISO-8601 strings, like `created_utc >= 2024-01-01`.
  - _Targeted Mining_: Target specific topics with keyword groupings (`has`, `has_all`) or regular expressions (`title ~= \bbot\b`).
- **Field Projections**: Keep output datasets lightweight and clean by extracting only the schema columns you need (e.g., `--fields id,title,score,author`).

### Instant Pandas & R Integrations

- **Diverse Output Formats**: Stream outputs directly to `jsonl` (preferred for streaming/Pandas), standard `json`, `csv` (for R/Excel), or rich console tables and Markdown reports.
- **Multi-Sink Pipeline**: Write the raw data to a `.jsonl` database while simultaneously writing a preview to a `.csv` summary in a single pass.

### Built-in Scientific Rigor

- **Crawl Manifests**: Every execution automatically generates a `.manifest.json` detailing exact parameters, versioning, records filtered, and a config fingerprint, preventing configuration drift in research environments.
- **Deterministic Sampling**: Extract reproducible subsets of huge subreddits using systematic or randomized sampling (e.g., Bernoulli trial at `rate = 0.1` with a fixed seed).

## Installation

Requires Python 3.12 or later and a [Reddit API application](https://www.reddit.com/prefs/apps) (free, read-only access is sufficient for most use cases).

### Via PyPI (Recommended)

Install the package directly using `pip` or `pipx`:

```bash
pip install praw-cli
```

### From Source (Using `uv`)

If you want to run it locally or contribute to development:

```bash
git clone https://github.com/othonhugo/praw-cli
cd praw-cli
uv sync
source .venv/bin/activate
```

## Documentation

Full documentation is available in the `docs/` directory.

- **[Getting Started](docs/getting-started.md)**: Installation and Authentication
- **Usage Guide**:
  - [Commands](docs/usage/commands.md)
  - [Pipelines & Filters](docs/usage/pipelines-filters.md)
  - [Formatters & Outputs](docs/usage/outputs.md)
  - [Scientific Use & Reproducibility](docs/usage/reproducibility.md)
- **Development**:
  - [System Architecture](docs/development/architecture.md)
  - [Decision Log (ADR)](docs/development/decisions.md)
  - [Contributing Guide](docs/development/contributing.md)
