# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# For native deps when needed (psycopg2-binary works without this, but keeps future-proof)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && pip install --no-cache-dir gunicorn

# Copy app source
COPY app/ /app/app

# Non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8000
# If your package is "app" and __init__.py re-exports `app`, this works:
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
