#!/bin/bash

# Generate a strong secret key
SECRET_KEY=$(openssl rand -base64 42)

# Create the superset_config.py file
cat << EOF > superset_config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://superset:superset@localhost:5432/superset'
SECRET_KEY = '$SECRET_KEY'
EOF

# Build and start the Docker Compose stack
docker-compose up -d