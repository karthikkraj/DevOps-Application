# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /worker

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the worker script
COPY worker.py .

# Command to run the worker script
CMD ["python", "worker.py"]

