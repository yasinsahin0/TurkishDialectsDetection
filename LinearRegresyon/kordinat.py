import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

class PathPredict:
    def __init__(self):
        self.dataset = pd.read_csv('data/kordinat.csv')
        self.X = self.dataset.iloc[:, :-1].values # tek sütun olsada bir matris onu vektöre çevirdik
        self.y = self.dataset.iloc[:, 1].values # bir vektör olduğu için stünü direk aldık

    def predict(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size = 1/3, random_state = 1)
        regressor = LinearRegression() # lineer reg sınıfından nesne oluşturuyoruz.
        regressor.fit(X_train, y_train) # model eğitimi yapıyoruz
        a = regressor.predict(y_test)
        print(a)
        print(y_test)
        asd = accuracy_score(y_test,a)
        #return regressor.predict(np.array([[value]]))

nsne = PathPredict()
nsne.predict()

"""
la =[365,367,370]
lb =[]

genelx = []
genely = []
for i in la:
    lb.append(nsne.predict(i))


genelx.append(int(nsne.X[0]))
genelx.append(la[-1])


genely.append(int(nsne.y[0]))
genely.append(lb[-1])

fig = plt.figure(figsize=(10,10))
plt.plot(list(nsne.y),list(nsne.X)) # ilk parametre x ekseni ikinci parametre y ekseni
plt.plot(la,lb,'r--')
plt.plot(genelx,genely,'k')
plt.show()
"""