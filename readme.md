# Siegenia Scraper

This is a web scraper built using Scrapy to extract product information from the [Siegenia online shop website](https://shop.siegenia.com/).

## Table of Contents
- [Siegenia Scraper](#siegenia-scraper)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Contributing](#contributing)

## Introduction
This scrapy scraper extract basic product details from the Siegenia online shop, including product names, SKUs, prices, and URLs.

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/stoeppke/siegenia-onlineshop-crawler.git
    cd siegenia
    ```

2. Install the required dependencies:
    ```bash
    pip install scrapy beautifulsoup4
    ```

3. Run the spider:
    ```bash
    scrapy crawl siegenia_spider -o output.jsonl
    ```

4. Remove duplicates from the output file:
    ```bash
    cat output.jsonl | sort | uniq > output_unique.jsonl
    ```

## Usage
The spider starts from a initial URL and follows counts the pages up until no more results are returned.

## Contributing
Feel free to contribute to the project by opening issues or pull requests. Your contributions are welcome!
This repo is using pre-commit hooks to ensure code quality. To install the pre-commit hooks, run:
```bash
pre-commit install
```
and to check the code before committing, run:
```bash
pre-commit run --all-files
```
