import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

colm_name = ['prregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
data = pd.read_csv("diabetes.csv")
data.columns = colm_name

feature_colm = ['prregnant','glucose','bp','skin','insulin','bmi','pedigree','age']
X = data[feature_colm]
y = data.label

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

desct = DecisionTreeClassifier()
desct = desct.fit(X_train,y_train)
y_pred = desct.predict(X_test)

print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))