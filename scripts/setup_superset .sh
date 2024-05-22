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

# Apache Superset installation using docker  compose
echo "Cloning the Apache Superset repository..."
git clone https://github.com/apache-superset/incubator-superset.git
cd incubator-superset

cat << EOF > docker-compose.yml
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: superset
      POSTGRES_PASSWORD: superset
      POSTGRES_DB: superset
    volumes:
      - superset-db:/var/lib/postgresql/data
  superset:
    image: apache/superset:latest
    environment:
      SUPERSET_DATABASE_URL: postgresql://superset:superset@db/superset
    ports:
      - 8080:8088
    depends_on:
      - db
volumes:
  superset-db:
EOF

echo "Starting Apache Superset using docker-compose..."
docker-compose up