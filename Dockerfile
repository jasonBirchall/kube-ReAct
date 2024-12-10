FROM python:3.12.0-slim

# Copy UV binary from its official container
COPY --from=ghcr.io/astral-sh/uv:0.5.7 /uv /bin/

# Set up a non-root user
RUN groupadd -g 1000 appgroup && \
  useradd -m -u 1000 -g appgroup appuser

# Set the working directory and user environment
WORKDIR /app
ENV HOME=/app
ENV UV_CACHE_DIR=/app/.cache/uv

# Pre-create and set ownership for necessary directories
RUN mkdir -p $UV_CACHE_DIR && chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Copy dependency files
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

# Install only the dependencies for better caching
RUN uv sync --frozen --no-install-project

# Copy application code
COPY app app
COPY example-data data
COPY data/production production

# Final sync to install the project
RUN uv sync --frozen

# Expose the application's port
EXPOSE 4567

# Run the application as the non-root user
CMD ["uv", "run", "gunicorn", "--bind=0.0.0.0:4567", "app.run:app"]
