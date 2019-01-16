# Azure Exception Fetcher

A quick script to fetch exceptions from a table located on a CosmosDB Table.

## Installation

```sh
pipenv sync
```

## Usage

Populate your environment:

```sh
echo "export COSMOSDB_ACCOUNT='<Your storage name>'" > .env
echo "export COSMOSDB_KEY='<Your storage key>'" >> .env
```

and Run:

```sh
LOG_ENV='dev' pipenv run ./scrape.py
```

You can also set the table name explicitly

```sh
export LOG_TABLE='devinformationlogs'
pipenv run ./scrape.py
```
