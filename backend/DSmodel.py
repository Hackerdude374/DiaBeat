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

pickle.dump(knn, open('example_weights_knn.pkl', "wb"))



#this will be called in app.py



















# The above code prepares the dataset and trains a KNN classifier to predict diabetes outcomes.
# Here's how it relates to your application:
# - We're using the Pima Indians Diabetes Database from Kaggle, which contains various health parameters.
# - The features (X) include attributes such as glucose level, blood pressure, BMI, etc.
# - The target variable (y) is the diabetes outcome (0 for non-diabetic, 1 for diabetic).
# - We split the dataset into training and testing sets to evaluate the model's performance.
# - We use a KNN classifier to predict diabetes outcomes based on the input features.
# - The trained model will be used in your application to m
