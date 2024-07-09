from flask import Flask, request, render_template
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load models and scaler
knn_model = pickle.load(open("knn_model.pkl", "rb"))
xgb_model = pickle.load(open("xgboost_model.pkl", "rb"))
logreg_model = pickle.load(open("logistic_regression_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def template_deploy():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert input values to floats
        input_1 = float(request.form['1'])
        input_two = float(request.form['2'])
        input_three = float(request.form['3'])
        input_four = float(request.form['4'])
        input_five = float(request.form['5'])
        input_six = float(request.form['6'])
        input_seven = float(request.form['7'])
        input_eight = float(request.form['8'])

        # Setup input data as a DataFrame with a Series
        setup_df = pd.DataFrame([pd.Series([input_1, input_two, input_three, input_four, input_five, input_six, input_seven, input_eight],
                                           index=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])])

        # Print input DataFrame for debugging
        print("Input DataFrame:\n", setup_df)

        # Scale the input data
        setup_df_scaled = scaler.transform(setup_df)

        # Print scaled DataFrame for debugging
        print("Scaled Input DataFrame:\n", setup_df_scaled)

        # Function to get model prediction
        def get_prediction(model, df, scaled=False):
            if scaled:
                prediction = model.predict_proba(df)
            else:
                prediction = model.predict_proba(setup_df)
            output = '{0:.2f}'.format(prediction[0][1], 2)
            print(f"Prediction for {model}: {prediction}")
            return str(float(output) * 100) + '%'

        # Make predictions using all three models
        knn_output = get_prediction(knn_model, setup_df_scaled, scaled=True)
        xgb_output = get_prediction(xgb_model, setup_df, scaled=False)
        logreg_output = get_prediction(logreg_model, setup_df_scaled, scaled=True)

        # Print model outputs for debugging
        print(f"KNN Output: {knn_output}, XGBoost Output: {xgb_output}, Logistic Regression Output: {logreg_output}")

        # Determine the best output based on the highest probability
        probabilities = [float(knn_output[:-1]), float(xgb_output[:-1]), float(logreg_output[:-1])]
        best_output = max(probabilities)

        if best_output > 50:
            message = f'You have the following chances of having diabetes based on our models:\n\nKNN: {knn_output}\nXGBoost: {xgb_output}\nLogistic Regression: {logreg_output}\n\nThe best model predicts a {best_output}% probability of having diabetes.'
        else:
            message = f'You have the following chances of having diabetes based on our models:\n\nKNN: {knn_output}\nXGBoost: {xgb_output}\nLogistic Regression: {logreg_output}\n\nThe best model predicts a low probability of diabetes, which is currently considered safe (this is only an example, please consult a certified doctor for any medical advice).'

        return render_template('result.html', pred=message)
    except ValueError:
        return render_template('result.html', pred='Invalid input. Please enter valid numbers.')

if __name__ == '__main__':
    app.run(debug=True)
