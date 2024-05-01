# https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

# KNN model user input predict diabetes. (K nearest neighors)
#KNN classifies data points based on points most similar to it
#guess or uneducated guess on what a unclassified data point should be classified as 
#--------------------------------------------------------
# Imagine we have a group of pets, some are cats, and some are dogs.
# We measure two things about them: their weight and height.
# We also know whether each one is a cat or a dog.
# Now, we want to teach the computer to guess whether a new pet is a cat or a dog
# based on its weight and height.

# Import necessary libraries
import numpy as np 
import pandas as pd  
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from flask import Flask, render_template, request

# Read the dataset (CSV file) into a pandas DataFrame
df = pd.read_csv('diabetes.csv')


# Separate the features (X) and target variable (y) from the DataFrame
X = df.drop('Outcome', axis=1) #- When we use `axis=1` in `df.drop('Outcome', axis=1)`, we're specifying that the operation
#   should be performed along columns (i.e., drop the 'Outcome' column).
# - In this case, `axis=1` indicates that we're dropping a column from the DataFrame.
y = df['Outcome']                # Target variable (class labels)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # Here, `test_size=0.2` means that 20% of the data will be used for testing, and the remaining

# Initialize a KNN classifier
knn = KNeighborsClassifier()

# Train the classifier using the training data
knn.fit(X_train, y_train)

# knn_score = knn.score(X_test, y_test)

#pickle data to serialize the file then deserialize it back (save model as pickle file)

model = pickle.load(open("example_weights_knn.pkl", "rb"))


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
        return render_template('result.html', pred=f 'You have the following chance of diabetes based on our KNN model is {output} ')
    else:
     return render_template('result.html', pred=f 'you have a low chance of diabetes which is currently considered good your probability is {output} ')
    
if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port = 80)
    app.run(debug=True) #default flask port







# The above code prepares the dataset and trains a KNN classifier to predict diabetes outcomes.
# Here's how it relates to your application:
# - We're using the Pima Indians Diabetes Database from Kaggle, which contains various health parameters.
# - The features (X) include attributes such as glucose level, blood pressure, BMI, etc.
# - The target variable (y) is the diabetes outcome (0 for non-diabetic, 1 for diabetic).
# - We split the dataset into training and testing sets to evaluate the model's performance.
# - We use a KNN classifier to predict diabetes outcomes based on the input features.
# - The trained model will be used in your application to m
