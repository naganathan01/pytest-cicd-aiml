# Fixed Dockerfile
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port for metrics
EXPOSE 8000

# Default command to run metrics exporter (not both commands)
CMD ["python", "metrics_exporter.py"]