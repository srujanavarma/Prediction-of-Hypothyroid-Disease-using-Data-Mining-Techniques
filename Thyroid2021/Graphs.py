import numpy as np
import matplotlib.pyplot as barg

import sys


class graph:
        
        def view(rlist):
                height=rlist
                hh = ( 'SVM','Naive Bayes', 'KNN','DT','NN')
                y_pos = np.arange(len(hh))
                barg.bar(hh, height, color=['red', 'green', 'blue', 'yellow','cyan'])
                #bar.plot( bars, height )
                barg.xlabel('Algorithms')
                barg.ylabel('Accuracy')
                barg.title('Prediction Accuracy Analysis')
                barg.show()





