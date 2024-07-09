from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Load all three models
knn_model = pickle.load(open("knn_model.pkl", "rb"))
xgb_model = pickle.load(open("xgboost_model.pkl", "rb"))
logreg_model = pickle.load(open("logistic_regression_model.pkl", "rb"))

@app.route('/')
def template_deploy():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    input_1 = request.form['1']
    input_two = request.form['2']
    input_three = request.form['3']
    input_four = request.form['4']
    input_five = request.form['5']
    input_six = request.form['6']
    input_seven = request.form['7']
    input_eight = request.form['8']

    # Setup input data as a DataFrame
    setup_df = pd.DataFrame([pd.Series([input_1, input_two, input_three, input_four, input_five, input_six, input_seven, input_eight])])

    # Make predictions using all three models
    knn_prediction = knn_model.predict_proba(setup_df)
    xgb_prediction = xgb_model.predict_proba(setup_df)
    logreg_prediction = logreg_model.predict_proba(setup_df)

    # Get the probability of having diabetes for each model
    knn_output = '{0:.{1}f}'.format(knn_prediction[0][1], 2)
    xgb_output = '{0:.{1}f}'.format(xgb_prediction[0][1], 2)
    logreg_output = '{0:.{1}f}'.format(logreg_prediction[0][1], 2)

    # Convert probabilities to percentages
    knn_output = str(float(knn_output) * 100) + '%'
    xgb_output = str(float(xgb_output) * 100) + '%'
    logreg_output = str(float(logreg_output) * 100) + '%'

    # Determine the best output based on the highest probability
    best_output = max(float(knn_output[:-1]), float(xgb_output[:-1]), float(logreg_output[:-1]))

    if best_output > 50:
        return render_template('result.html', pred=f'You have the following chances of having diabetes based on our models:\n\nKNN: {knn_output}\nXGBoost: {xgb_output}\nLogistic Regression: {logreg_output}\n\nThe best model predicts a {best_output}% probability of having diabetes.')
    else:
        return render_template('result.html', pred=f'You have the following chances of having diabetes based on our models:\n\nKNN: {knn_output}\nXGBoost: {xgb_output}\nLogistic Regression: {logreg_output}\n\nThe best model predicts a low probability of diabetes, which is currently considered safe (this is only an example, please consult a certified doctor for any medical advice).')

if __name__ == '__main__':
    app.run(debug=True)