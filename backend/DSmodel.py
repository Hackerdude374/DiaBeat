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

import numpy as np 
import pandas as pd  
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

