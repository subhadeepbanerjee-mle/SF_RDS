import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('./Models/model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/predict')
def predict():
	'''
	For rendering results on HTML GUI
	'''
	value = request.args.get('value')
	prediction = model.predict(np.array([value]).reshape(-1, 1))
	output = round(prediction[0], 2)
	return f'the result is {output}!'

if __name__ == '__main__':
	app.run('localhost', 5000)
