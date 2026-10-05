# Python and Data Engineering Learning Lab

A collection of small, runnable lessons. Each example is meant to teach one idea; this is a learning repository, not a production application.

## Start here

Use Python 3.12 or newer. The project uses `uv` for its environment and dependency lock:

```powershell
uv sync
```

Run a lesson from the repository root. For example:

```powershell
python python/fundamentals/core_types.py
python -m data_engineering.batch_pipeline
```

The batch pipeline reads the included orders CSV, validates its rows, and loads them into `data_engineering/orders.sqlite3`. Pass `--input` and `--database` to choose other paths. The output database is generated data and should not be committed.

## Learning map

| Path | Topics |
| --- | --- |
| `python/fundamentals/` | Built-in collections, functions, generators, exceptions, files, context managers, logging |
| `python/oop/`, `python/inheritance/`, `python/polymorphism/` | Classes, encapsulation, inheritance, decorators, polymorphism |
| `python/concurrency/asyncio/`, `python/concurrency/threading/` | Coroutines, concurrent tasks, threads, and when blocking work matters |
| `python/os/` | Paths, directories, and filesystem inspection |
| `data_engineering/` | Record validation, CSV extraction, batch loading, SQLite tables, transactions, upserts, basic pipeline metrics, pandas file-format examples |
| `testing/` | Pytest assertions, error checks, classes, parameterized tests, and mocks |
| `data_engineering/apis/` | Requests, HTTP methods, headers, parameters, and authentication in a notebook |
| `data_engineering/pydantic/` | Pydantic models, fields, strict types, validation, and serialization notebooks |

The API notebook includes live HTTP calls and placeholder credentials. Run cells selectively; the URLs and credentials are examples. Parquet examples require a pandas parquet engine such as PyArrow, which is not currently declared as a project dependency.

## Coverage audit

This repository currently gives introductory coverage of Python collections and functions, object-oriented programming, common concurrency patterns, HTTP requests, typed validation, basic pandas file reads, testing, and a small batch ETL flow.

It is not yet a complete Python or data engineering curriculum. The next useful areas to add are SQL joins and window functions, database connection/configuration management, pipeline-specific tests and expanded data-quality suites, structured logging and retry/backoff, columnar formats and partitioning, orchestration, cloud object storage, Spark, and streaming systems. Those larger tools should be introduced in focused lessons when they are part of the intended learning path, rather than represented by toy code as if they were fully covered here.

## Conventions

- Keep lesson paths lowercase with `snake_case` filenames.
- Keep reusable functions free of work at import time; put demonstrations behind `if __name__ == "__main__":`.
- Resolve sample files relative to the lesson file, not the shell's current directory.
- Keep credentials out of source files; use environment variables for real integrations.
