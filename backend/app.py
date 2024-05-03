from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import pickle

app = Flask(__name__) 

model = pickle.load(open("example_weights_knn.pkl", "rb"))

#when u visit websites, its index.html



@app.route('/')
def use_template():
    return render_template("index.html") #frontend calling

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    input_1 = request.form['1']
    input_2 = request.form['2']
    input_3 = request.form['3']
    input_4 = request.form['4']
    input_5 = request.form['5']
    input_6 = request.form['6']
    input_7 = request.form['7']
    input_8 = request.form['8']

    # Setup input data as a DataFrame
    setup_df = pd.DataFrame([[input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8]])

    # Make predictions using the loaded model
    diabetes_prediction = model.predict_proba(setup_df)
    output = '{0:.{1}f}'.format(diabetes_prediction[0][1],2)
    output = str(float(output)*100) + '%'
    

    # Decide prediction based on probability threshold
    if output >str(0.5):
        return render_template('result.html', pred=f'You have the following chance of diabetes based on our KNN model is {output} ')
    else:
     return render_template('result.html', pred=f'you have a low chance of diabetes which is currently considered good your probability is {output} ')
    
    
    
# debugging 
app = Flask(__name__)

@app.route('/')

def index(): #index.html
    
    if __name__ == '__main__':
        
        app.run(debug=True)
        
print(app.debug) # should print True