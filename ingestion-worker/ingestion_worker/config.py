import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://nextbatch:change_me_locally@localhost:5432/nextbatch",
)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")