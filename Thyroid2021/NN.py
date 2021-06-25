# importing packages

import numpy.random as numrandom
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


from sklearn import metrics
from featuresel import featureselection


class NN:
    def accuracy(self):
        attr = featureselection.calc("hypothyroid.csv")
        attr.append('result')

        datainput = pd.read_csv("hypothyroid.csv")
        x_train = datainput[attr]

        print(x_train)
        y = datainput['result']
        del datainput['result']

        # Split data into Test & Training Dataset
        # Testing data is 30% & Training data is 70%
        x_train, x_test, y_train, y_test = train_test_split(datainput, y, test_size=0.3)

        nn = MLPClassifier()
    # Training the model
        nn.fit(x_train, y_train)
    # Use the model on the Testing data
        predicted5 = nn.predict(x_test)
        print("NN Accuracy Score:")
    # Calculate the accuracy
        accurcy = metrics.accuracy_score(y_test, predicted5)


      # Printing the accuracy
        print(accurcy)
        print('')
        print('')
    # Turns to % for graph representation.
        return accurcy

if __name__ == "__main__":
    n = NN()
    print(n.accuracy())
