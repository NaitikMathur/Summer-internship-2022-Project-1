# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 23:55:04 2022

@author: Punit
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('Summer internship 2022 Project 1.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    sqft = float(request.args.get('sqft'))
    
    prediction = model.predict([[sqft]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted price for given squarefeet is : {}'.format(prediction))


app.run(debug=True)