# Flipkart Product Price Predictor
#### Data was obtained from kaggle [Flipkart E-commerce Dataset](https://www.kaggle.com/datasets/atharvjairath/flipkart-ecommerce-dataset)
### Problem Statement
The goal of the project is to predict the retail price of products.Predicting the price of products will be helpful for users to make better decisions.

## Table of Contents

- [Project Structure](#projectstr)
- [Data](#data)
- [Running The Project](#run)
- [Local Deployment](#deploy)
- [Example](#example)
- [Cloud Deployment](#cloud) 


## Project Structure
1. [ReadME.md](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/README.md): contains all the information about the project.

2. [notebook.ipynb](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/notebook.ipynb) : contains the following  
 * Data ingestion and preparation
 * Exploratory Data Analysis
 * feature engineering and selection
 * model training, hyperparameter optimization and model selection

3. [model_C=1.0.bin](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/model_C=1.0.bin) : final model in pickle format
   
4. [train.py](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/train.py): python script that trains the final selected model

5. [predict.py](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/predict.py) : flask api that serves the final result of model

6. [requirements.txt](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/requirements.txt) : file containing the required dependencies that have to be installed for the local enviroment

7. [Dockerfile](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/Dockerfile) : file with instruction on how to containerize the project.r

8. [test.ipynb](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/test.py) : script used to test the final model

9. [Test Data](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/blob/main/test) : contains json values of records for test purposes 

## Data
About dataset
This is an E-commerce Flipkart Dataset with exactly 20,000 samples. It has 15 columns with a lot of information. You can use it to predict price of products of predict which category a product might fall under.
  
Contents
* This dataset contains Flipkart Ecommerce Data in CSV format: 
* The Retail_Price table contains information on all 20,000 products from Flipkart Ecommerce Site.
* Each record represents one product, and contains details about their description, retail_price, discount_price,image, etc.

## Running The Project

#### Create new folder
```
mkdir [name_of_your_folder] && cd [name_of_your_folder]
```
#### clone this repository:
```
https://github.com/sam47-asfaw/Flipkart-Price-Predictor.git
```
#### create anaconda enviroment:
```
conda create -p name_of_your_env python==(python_version) -y
```

#### acivate your enviroment
```
conda activate name_of_your_env
```

#### install the dependencies
cd into your_proj_folder
```
pip install -r requirements.txt
```
#### train the model
```
python train.py
```
#### run the model
##### open the terminal,cd into your project folder and run the following instruction
```
waitress-serve --listen=0.0.0.0:8080 predict:app
```
## Deployment
#### Deploy the model locally:
* cd into the main_project_folder
* make sure docker engine is running
```
docker build -t your_container_name .
```
```
docker run -it --rm -p 8080:8080 your_container_name
```
#### test the model
#### open test.ipynb and test the model
#### make sure to substitute the url with the 'http:\localhost\8080\predict'

## Example
Here is an example of what the output will look like after deployed locally
![reg_result](https://github.com/sam47-asfaw/Flipkart-Price-Predictor/assets/62788450/a0bc82ce-3320-4728-968f-33064ba3039a)
)

## Cloud Deployment
#### Deploy the model as Flask API on Google Cloud API
##### Install [google cloud sdk](https://cloud.google.com/sdk/docs/install)
##### Set up your profile on Google Cloud Platform 
##### Create your first project and enable Cloud Run and Cloud Build API's
##### open the terminal and be on the same folder as Dockerfile and run the following instructions
```
gcloud builds submit --tag gcr.io/your_project_id/predict
```
```
gcloud run deploy --image gcr.io/your_project_id/predict --platform managed
```
##### select the appropriate region, fill out appropriate api name and choose y
## Test deployed API
##### Exchange the google cloud plaform generated url in the test.ipynb and test it. 




