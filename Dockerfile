FROM python:3.8-slim

# Set workdir
WORKDIR /app

# Install system-level build dependencies
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        gcc \
        g++ \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender-dev \
        awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (enables Docker cache)
COPY requirements.txt .

# Install Python dependencies (except -e .)
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application code
COPY . .

# Install your local package in editable mode
RUN pip install -e .

# Expose port if needed
EXPOSE 8080

# Run your app
CMD ["python3", "application.py"]
