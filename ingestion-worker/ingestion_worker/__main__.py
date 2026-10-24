import argparse
from ingestion_worker.log import setup_logging
from ingestion_worker import db


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ingestion_worker", description="NextBatch ingestion worker"
    )
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("check-db", help="Verify the database connection")
    sub.add_parser("run", help="Run all enabled sources once (added later)")
    args = parser.parse_args()
    log = setup_logging()

    if args.cmd == "check-db":
        try:
            log.info("DB connection OK" if db.check_connection() else "DB check failed")
        except Exception as e:
            log.error("Cannot connect to the database: %s", e)
            raise SystemExit(1)
    elif args.cmd == "run":
        log.info("Not implemented yet (feat/ingest-first-adapter)")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()