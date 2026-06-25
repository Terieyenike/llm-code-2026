# AIHero Course

Welcome to the **AIHero Course**! This directory contains the code and resources for hands-on AI learning through practical exercises and guided examples.

## Overview

This course is structured in modules and daily exercises that combine foundational concepts in AI with real code. You'll work with tools and datasets commonly used in the field.

### What’s in this folder?

- **`fm.md`**: Markdown file with YAML front matter metadata.
- **`day1.py`**: Script that demonstrates a complete pipeline for downloading GitHub repositories as zip files, parsing frontmatter metadata, and extracting textual content from markdown files.
- **`pyproject.toml`**: Project configuration and dependency management.

## Setup Instructions

We use [uv](https://github.com/astral-sh/uv) (a fast Python package manager) instead of pip.

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd aihero/course
   ```

2. **Install dependencies with uv**
   ```bash
   uv pip install -r requirements.txt
   ```
   Or, for editable installs:
   ```bash
   uv pip install .
   ```

3. **Run the Day 1 Demo**
   ```bash
   python day1.py
   ```

## Day 1: Data Ingestion Pipeline

On Day 1, you’ll build and run a pipeline that can:
- Download a GitHub repository as a zip archive,
- Parse metadata from markdown files using frontmatter,
- Extract and display main content from those files.

This experience gets you familiar with programmatically working with real-world documentation as a data source.

---

**Happy learning!**
