import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier

class featureselection:
	def calc(filepath):
		data = pd.read_csv(filepath)
		X = data.iloc[:,0:15]  
		y = data.iloc[:,16]    
		
		model = ExtraTreesClassifier()
		model.fit(X,y)
		print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
		#plot graph of feature importances for better visualization
		feat_importances = pd.Series(model.feature_importances_, index=X.columns)
		feat_importances.nlargest(7)
		d=dict(feat_importances.nlargest(7))
		l=[]
		for ll in d:
			#print(ll)
			l.append(ll)

		#plt.show()
		return l



if __name__=="__main__":
	print(featureselection.calc())
