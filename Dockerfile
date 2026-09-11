# ============================================================
# File:        Dockerfile
# Description: Cloud Run container for AxisOS Bio‑Rhythm Engine
# Version:     2.0
# ============================================================

FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source + Gemini config
COPY biorhythm_engine.py main.py agent.yaml manifest.json tools.json ./

ENV PORT=8080

CMD ["python", "main.py"]
