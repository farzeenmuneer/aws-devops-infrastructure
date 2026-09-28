
# STAGE 1: Builder

FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# STAGE 2: Runtime

FROM python:3.12-slim

# Create non-root user for security
RUN useradd -m -u 1001 appuser

WORKDIR /app

# Copy only installed dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY app.py .

# Set PATH for user-installed packages
ENV PATH=/home/appuser/.local/bin:$PATH
ENV APP_VERSION=1.0.0

# Switch to non-root user
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]