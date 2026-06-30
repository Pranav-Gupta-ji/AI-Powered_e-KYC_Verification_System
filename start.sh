#!/bin/sh

echo "Starting FastAPI..."

uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000 &

sleep 10

echo "Starting Streamlit..."

exec streamlit run frontend/Home.py \
    --server.address=0.0.0.0 \
    --server.port=7860