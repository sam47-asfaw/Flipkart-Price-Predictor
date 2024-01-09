# Define base image
FROM python:3.11-slim

# Set working directory for the project
WORKDIR /app

# Get dependencies
COPY requirements.txt .

# Create and activate Conda environment
RUN apt-get update && \
    apt-get install -y curl && \
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    /miniconda/bin/conda create -p /venv python=3.11 -y && \
    echo "source /miniconda/bin/activate /venv" >> ~/.bashrc

# Activate Conda environment
SHELL ["/bin/bash", "--login", "-c"]

# Download the dependencies:
RUN source ~/.bashrc && /venv/bin/pip install -r requirements.txt

# Copy application files
COPY ["model_reg=1.0.bin", "predict.py", "./"]

# Expose the port
EXPOSE 9696

# Command to run the application
CMD ["/venv/bin/waitress-serve", "--host=0.0.0.0", "--port=9696", "predict:app"]
