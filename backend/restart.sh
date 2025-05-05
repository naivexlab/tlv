#!/bin/bash
set -e

cd backend

echo "Restarting FastAPI Backend..."

pkill -f "uvicorn main:app" || echo "No previous backend process running."

# install dependencies
pip install -r requirements.txt

# Start FastAPI backend in development mode
uvicorn main:app --host 127.0.0.1 --port 8000 --reload &

echo "FastAPI backend is running!"