  # Use official Python image as base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy all local files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5050
EXPOSE 5050

# Run the Flask app
CMD ["python3", "app.py"]

