# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install git and cleanup in one layer for efficiency
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt without caching them
RUN pip install --no-cache-dir -r requirements.txt

# Non-root user setup: create a user 'camoo' and switch to it
RUN adduser --disabled-password --gecos "" camoo
USER camoo
