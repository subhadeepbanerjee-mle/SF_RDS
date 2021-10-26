# Deploying ML Model using Flask
## Prerequisites
This is a simple project to elaborate how to deploy a Machine Learning model using Flask
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask installed.

## Project Structure
This project has two major parts :

model.py - This contains code for downloading of diabetes dataset for Machine Learning model to predict one of the value 
flask_server.py - This contains Flask server that receives the deseriesed model and computes the precited value.
Models- This folder contains the seriesed ML model

## Running the model
Please be sure that the flask server is running.
Navigate the URL http://localhost:5000/predict?value=1 in case if input value is 1
In other case you can use another value.
