import pandas as pd

# Load the cleaned dataset
data = pd.read_csv('cleaned_diabetes.csv')

# Check the class distribution
class_counts = data['Outcome'].value_counts()
print(class_counts)