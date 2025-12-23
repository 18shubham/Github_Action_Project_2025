FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the app (host 0.0.0.0 is critical for Docker!)
CMD ["python", "app.py"]
