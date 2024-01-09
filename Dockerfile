# Define base image
FROM python:3.11-slim

# Set working directory for the project
WORKDIR /app

#create conda enviroment
RUN conda create -p venv python==3.11 -y

#activate virtual enviroment
RUN conda activate nenv/

# Get dependencies
COPY requirements.txt .

# Download the dependencies:
RUN pip install -r requirements.txt

COPY ["model_reg=1.0.bin", "predict.py", "./"]

EXPOSE 9696

CMD ["waitress-serve","--host=0.0.0.0","--port=9696","predict:app"]