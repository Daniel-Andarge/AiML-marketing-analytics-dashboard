#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Installing Docker..."
    # Install Docker 
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi

# Pull the latest Redash image
echo "Pulling the latest Redash image..."
docker pull redash/redash:latest

# Start the Redash container
echo "Starting the Redash container..."
docker run -d -p 5000:5000 \
           -e REDASH_DATABASE_URL="postgresql://redash:redash@postgres/redash" \
           -e REDASH_REDIS_URL="redis://redis:6379/0" \
           --name redash redash/redash:latest

echo "Redash server is now running on port 5000."

# Create a Postgres container for Redash
echo "Creating a Postgres container for Redash..."
docker run -d --name postgres \
           -e POSTGRES_USER=redash \
           -e POSTGRES_PASSWORD=redash \
           -e POSTGRES_DB=redash \
           postgres:12

# Create a Redis container for Redash
echo "Creating a Redis container for Redash..."
docker run -d --name redis redis:5

echo "Redash setup is complete. You can access the Redash dashboard at http://localhost:5000."