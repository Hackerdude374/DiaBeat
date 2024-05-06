# Diabetes Prediction Application

This is a web application for predicting diabetes using a KNN model. The application allows users to input various health parameters and receive a prediction of whether they are likely to have diabetes or not.

## Setting up the App

Navigate to Visual Studio Code (VSCode) and make sure you are running it as an administrator.

1. run git pull in the main directory of the project (in my case its Diabeat) to get the latest changes.
 ```
 git pull
```
2. or just in case run 
```
git pull origin
```

3. Navigate to the `\frontend ` directory of the project, and run this to ensure you get the latest packages/libraries.
```
npm i --force
```
 
4. Navigate to the `\backend` directory of the project and run this to ensure you get the patest packabges/libraries.
```
pip install --upgrade --force-reinstall -r installed_packages.txt

```

## Running the Application

### Backend

1. Open a terminal and navigate to the `/backend` directory of the project.

2. Start the Flask server by running:
    ```
    $ flask run
    ```
   Alternatively, you can use:
    ```
    $ python -m flask run
    ```

### Frontend

1. Open a new terminal window/tab.

2. Navigate to the `/frontend` directory of the project.

3. Start the frontend development server by running:
    ```
    $ npm start
    ```

## Debugger Setup

To enable the debugger while running the application, follow these steps:

1. In the terminal where you're running the Flask backend, set the Flask debug mode:
    ```
    $ export FLASK_DEBUG=1
    ```
    Or in powershell:
    ```
    $env:FLASK_DEBUG = 1
    ```

2. Verify that debug mode is properly set by running:
    ```
    $ echo $FLASK_DEBUG
    ```
   The output should be `1`.

3. Now, run the Flask server as usual:
    ```
    $ flask run
    ```
   or:
    ```
    $ python -m flask run
    ```

With the debugger properly set up, you can now debug your Flask application effectively.

## KNN Model Overview

The K Nearest Neighbors (KNN) algorithm is a simple and effective machine learning algorithm used for classification and regression tasks. In the context of this application, the KNN model is trained to predict whether an individual is likely to have diabetes based on their health parameters.

### How KNN Works

1. **Training the Model:**
   
   - The KNN model is trained using a dataset of known diabetes outcomes and corresponding health parameters. This dataset is typically split into a training set and a testing set.
   
   - During training, the model stores the training data in memory, essentially memorizing the feature vectors and their corresponding labels.

2. **Making Predictions:**
   
   - When presented with new, unseen data (i.e., input from the user), the KNN algorithm calculates the distance between the input data point and all other data points in the training set.
   
   - It then selects the K nearest neighbors (data points with the smallest distances) to the input data point.

3. **Classification:**
   
   - For classification tasks like predicting diabetes, the KNN algorithm assigns a label to the input data point based on the majority class among its K nearest neighbors.
   
   - For example, if the majority of the K nearest neighbors have diabetes (label 1), the algorithm predicts that the input data point also has diabetes. Otherwise, it predicts that the input data point does not have diabetes (label 0).

### KNN Model Training Example

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Read the dataset (CSV file) into a pandas DataFrame
df = pd.read_csv('diabetes.csv')

# Separate the features (X) and target variable (y) from the DataFrame
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize a KNN classifier
knn = KNeighborsClassifier()

# Train the classifier using the training data
knn.fit(X_train, y_train)