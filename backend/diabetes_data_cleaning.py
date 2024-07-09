import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the CSV file
data = pd.read_csv('diabetes.csv')

# Display the first few rows of the dataset
print("Original Dataset:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Replace zero values with NaN
data['Glucose'] = data['Glucose'].replace(0, np.nan)
data['BloodPressure'] = data['BloodPressure'].replace(0, np.nan)
data['SkinThickness'] = data['SkinThickness'].replace(0, np.nan)
data['Insulin'] = data['Insulin'].replace(0, np.nan)
data['BMI'] = data['BMI'].replace(0, np.nan)

# Fill missing values with the mean
data.fillna(data.mean(), inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Perform feature scaling (standardization)
scaler = StandardScaler()
columns_to_scale = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])

# Save the cleaned dataset to a new CSV file
data.to_csv('cleaned_diabetes.csv', index=False)

print("\nCleaned Dataset:")
print(data.head())