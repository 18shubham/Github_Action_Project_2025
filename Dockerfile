# STAGE 1: The Builder
# We use a full image to get all the tools needed to compile/install
FROM python:3.9-slim AS builder
WORKDIR /build
COPY requirements.txt .
# Install dependencies into a local folder
RUN pip install --user --no-cache-dir -r requirements.txt

# STAGE 2: The Final Image
# We start with a fresh, tiny image and only copy what is necessary
FROM python:3.9-slim
WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
# Copy the app code
COPY app.py .

# Ensure the app can find the installed packages
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["python", "app.py"]
