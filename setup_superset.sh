#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Installing Docker..."
    # Install Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
else
    echo "Docker is already installed."
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Installing Docker Compose..."
    # Install Docker Compose
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
else
    echo "Docker Compose is already installed."
fi

# Clone the Superset repository
if [ ! -d "incubator-superset" ]; then
    echo "Cloning the Superset repository..."
    git clone https://github.com/apache/superset.git incubator-superset
else
    echo "Superset repository already cloned."
fi

cd incubator-superset

# Copy the example Docker Compose file
cp docker-compose-non-dev.yml docker-compose.yml

# Start Superset
echo "Starting Superset using Docker Compose..."
docker-compose -f docker-compose.yml up -d 

# Initialize the database
echo "Initializing the database..."
docker-compose exec superset superset db upgrade
docker-compose exec superset superset init

echo "Superset setup completed."
echo "You can access Superset at http://localhost:8088 with default credentials (admin/admin)."