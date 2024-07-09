import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the cleaned dataset
data = pd.read_csv('cleaned_diabetes.csv')

# Separate features and target variable
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Experiment with different values for C and class weights
C_value = 0.1
class_weight = {0: 1, 1: 3}

# Initialize and train the Logistic Regression classifier
logreg_model = LogisticRegression(random_state=42, class_weight=class_weight, C=C_value)
logreg_model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred_train = logreg_model.predict(X_train_scaled)
y_pred_test = logreg_model.predict(X_test_scaled)
y_prob_test = logreg_model.predict_proba(X_test_scaled)

print("Training Accuracy:", accuracy_score(y_train, y_pred_train))
print("Test Accuracy:", accuracy_score(y_test, y_pred_test))
print("\nClassification Report (Test Data):\n", classification_report(y_test, y_pred_test))
print("Confusion Matrix (Test Data):\n", confusion_matrix(y_test, y_pred_test))
print("\nPredicted Probabilities (Test Data):\n", y_prob_test)

# Debug: Examine weights and intercept
print("\nModel Weights (Coefficients):\n", logreg_model.coef_)
print("Model Intercept:\n", logreg_model.intercept_)

# Delete existing model files if they exist
if os.path.exists('logistic_regression_model.pkl'):
    os.remove('logistic_regression_model.pkl')
if os.path.exists('scaler.pkl'):
    os.remove('scaler.pkl')

# Save the Logistic Regression model and scaler
pickle.dump(logreg_model, open('logistic_regression_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
