


import numpy.random as numrandom
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier




datainput = pd.read_csv("hypothyroid.csv")
testfile="testing.csv"

x_test=pd.read_csv(testfile)
print(x_test)
y = datainput['result']
del datainput['result']


# Split data into Test & Training Dataset
# Testing data is 30% & Training data is 70%

nn = MLPClassifier()
# Training the model
nn.fit(datainput, y)
# Use the model on the Testing data
predicted5 = nn.predict(x_test)

print(predicted5)


