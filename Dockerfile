FROM python:3.14-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential curl && \
    rm -rf /var/lib/apt/lists/*
RUN pip install uv
COPY pyproject.toml ./
COPY uv.lock ./
RUN uv sync --python-platform linux --frozen --all-extras

# Smaller runtime image (no build tools)
FROM python:3.14-slim AS runtime
WORKDIR /app
# Copy the installed Python packages from the builder stage
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY ./main.py .
COPY ./src ./src
EXPOSE 5000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
