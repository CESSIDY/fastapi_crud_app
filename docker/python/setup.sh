#!/bin/bash
set -eu
cd /var/app
poetry run alembic upgrade head

cd /src
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
