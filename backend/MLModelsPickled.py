import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# Load the dataset
df = pd.read_csv('cleaned_diabetes.csv')

# Separate features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train models
models = {
    "knn": KNeighborsClassifier(n_neighbors=5),
    "xgb": XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42),
    "logreg": LogisticRegression(C=0.1, class_weight={0: 1, 1: 3}, random_state=42),
    "rf": RandomForestClassifier(n_estimators=100, random_state=42)
}

for name, model in models.items():
    if name == "xgb":
        model.fit(X_train, y_train)
    else:
        model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled if name != "xgb" else X_test)
    print(f"{name.upper()} Model")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    pickle.dump(model, open(f"{name}_model.pkl", "wb"))

# Save the scaler
pickle.dump(scaler, open("scaler.pkl", "wb"))
