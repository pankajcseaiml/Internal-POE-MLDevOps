# Step 9: Pull lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Step 10: Add hello.py into Docker container
COPY hello.py .

# Run hello.py when container starts
CMD ["python", "hello.py"]

