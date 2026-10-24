import psycopg
from ingestion_worker import config


def connect() -> psycopg.Connection:
    return psycopg.connect(config.DATABASE_URL)


def check_connection() -> bool:
    with connect() as conn:
        return conn.execute("SELECT 1").fetchone()[0] == 1