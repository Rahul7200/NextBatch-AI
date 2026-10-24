import logging
from ingestion_worker import config


def setup_logging() -> logging.Logger:
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    return logging.getLogger("ingestion")