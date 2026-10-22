# FastAPI Microservice Template

A clean, asynchronous production boilerplate for building microservices using FastAPI, SQLAlchemy 2.0, Pydantic v2, and Docker.

## Features
- **Async First**: Full async support via `asyncpg` and SQLAlchemy async engine.
- **Structured Architecture**: Modular routers, dependency injection, and centralized error handling.
- **Configuration Management**: Type-safe settings via `pydantic-settings`.
- **Health Checks & Monitoring**: Built-in `/healthz` and readiness probes.

## Quick Start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
