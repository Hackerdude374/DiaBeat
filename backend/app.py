from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import pickle


app = Flask(__name__) 

model = pickle.load(open("example_weights_knn.pkl", "rb"))

#when u visit websites, its index.html



@app.route('/')
def use_template():
    return render_template("index.html") #frontend calling

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)

#------------------------------------------------------------------------------
    # input_1 = request.form['1']
    # input_2 = request.form['2']
    # input_3 = request.form['3']
    # input_4 = request.form['4']
    # input_5 = request.form['5']
    # input_6 = request.form['6']
    # input_7 = request.form['7']
    # input_8 = request.form['8']
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Dummy inputs for postman testing
    input_one = 5
    input_two = 120
    input_three = 80
    input_four = 30
    input_five = 100
    input_six = 25
    input_seven = 0.5
    input_eight = 40

    # Setup input data as a DataFrame
    setup_df = pd.DataFrame([[input_one, input_two, input_three, input_four, input_five, input_six, input_seven, input_eight]])

    # Make predictions using the loaded model
    diabetes_prediction = model.predict_proba(setup_df)
    output = '{0:.{1}f}'.format(diabetes_prediction[0][1], 2)
    output = str(float(output) * 100) + '%'

    # Decide prediction based on probability threshold
    if float(output) > 0.5:
        return render_template('result.html', pred=f'You have the following chance of diabetes based on our KNN model is {output} ')
    else:
        return render_template('result.html', pred=f'You have a low chance of diabetes which is currently considered good. Your probability is {output} ')

#----------------------------------------------------------------------------------------------

# debugging 
# app = Flask(__name__)

# @app.route('/')
# #index.html
# def index(): 
    
#     if __name__ == '__main__':
        
#         app.run(debug=True)
        
# # print(app.debug) # should print True