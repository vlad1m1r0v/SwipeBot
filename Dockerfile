# Stage 1: Build the image
FROM python:3.12-slim AS builder

# Set the working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install Poetry and export dependencies to requirements.txt
RUN pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes

# Copy all project files
COPY . .

# Stage 2: Create the final image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies from the requirements.txt file
COPY --from=builder /app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY --from=builder /app /app

# Define the command to run the bot
CMD ["python", "-m", "bot"]