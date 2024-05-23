#!/bin/bash


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

# Pull the latest Metabase image
echo "Pulling the latest Metabase image..."
docker pull metabase/metabase:latest

# Start the Metabase container
echo "Starting the Metabase container..."
docker run -d -p 3000:3000 --name metabase metabase/metabase

echo "Metabase server is now running on port 3000."