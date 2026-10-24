# NextBatch AI

Spring Boot API + React frontend + Python AI/RAG service + ingestion worker + PostgreSQL/pgvector.

## Modules
- frontend/ - React + TypeScript
- backend-java/ - Spring Boot API
- database/ - migrations and seed data
- ai-service-python/ - FastAPI AI/RAG service
- ingestion-worker/ - official-source ingestion
- infra/ - docker-compose
- docs/api-contracts/ - API contracts

## Rules
One folder per owner, one branch per task, small PRs, no direct push to main.
Each module has its own README with run steps.