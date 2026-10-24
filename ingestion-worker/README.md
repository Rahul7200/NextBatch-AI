# Ingestion Worker

Fetches opportunities from permitted official sources, normalizes them, removes duplicates
and writes them to PostgreSQL. Owner: Backend Dev 4.

## Setup
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    copy .env.example .env

## Run
    python -m ingestion_worker --help
    python -m ingestion_worker check-db
    python -m ingestion_worker run

## Test
    pytest -q

## Rules
Use only sources whose terms allow automated access. Unknown deadlines stay NULL.
Never write to tables owned by other modules (see docs/api-contracts/data-ownership.md).