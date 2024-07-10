import pandas as pd
from imblearn.over_sampling import SMOTE

# Load the cleaned dataset
data = pd.read_csv('cleaned_diabetes.csv')

# Separate features and target variable
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Apply SMOTE to balance the classes
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Check the class distribution after SMOTE
class_counts = pd.Series(y_resampled).value_counts()
print("Class distribution after SMOTE:")
print(class_counts)

# If you want to save the resampled data to a new CSV file
resampled_data = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name='Outcome')], axis=1)
resampled_data.to_csv('resampled_diabetes.csv', index=False)
