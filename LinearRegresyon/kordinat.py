import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('kordinat.csv')

X = dataset.iloc[:, :-1].values # tek sütun olsada bir matris onu vektöre çevirdik
y = dataset.iloc[:, 1].values # bir vektör olduğu için stünü direk aldık


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

regressor = LinearRegression() # lineer reg sınıfından nesne oluşturuyoruz.

regressor.fit(X_train, y_train) # model eğitimi yapıyoruz
#print(X_test)
a = np.array([[65],[80]])
print(a)
y_pred = regressor.predict(a)
print("X:65 te Tahmini Y değeri : "+str(y_pred[0]))
print("X:80 te Tahmini Y değeri : "+str(y_pred[1]))
