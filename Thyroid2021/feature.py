import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
class featureselection:
	
	def calc(filepath):
		print(filepath)
		data = pd.read_csv(filepath)
		X = data.iloc[:,0:15]  #independent columns
		y = data.iloc[:,16]    #target column i.e price range
		
		model = ExtraTreesClassifier()
		model.fit(X,y)
		print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
		#plot graph of feature importances for better visualization
		feat_importances = pd.Series(model.feature_importances_, index=X.columns)
		feat_importances.nlargest(15).plot(kind='barh')
		d=dict(feat_importances.nlargest(15))
		l=[]
		for ll in d:
			#print(ll)
			l.append(ll)

		plt.show()
		return l



if __name__=="__main__":
	print(featureselection.calc('hypothyroid.csv'))
