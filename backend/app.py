from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import pickle

app = Flask(__name__) 

model = pickle.load(open("example_weights_knn.pkl", "rb"))

#when u visit websites, its index.html




@app.route('/') #app route tell Flask 
def use_template():
    return render_template("index.html") # connect to frontend

# def greeting():
#     return 'Flask is awesome'
# API
 @app.route('/predict', methods = ['POST','GET'])
 def predict():
   input_1 = request.form['1']
input_2 = request.form['2']
input_3 = request.form['3']
input_4 = request.form['4']
input_5 = request.form['5']
input_6 = request.form['6']
input_7 = request.form['7']
input_8 = request.form['8']
