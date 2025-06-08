# Dockerfile
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Default command to run tests
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
