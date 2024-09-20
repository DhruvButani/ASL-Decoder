import pickle
import os 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

print('starting')
dataPickle = pickle.load(open('./data/data.pickle', 'rb'))


data = np.asarray(dataPickle['data'])
labels = np.asarray(dataPickle['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle = True, stratify=labels)

model = RandomForestClassifier(n_estimators=100)

model.fit(x_train, y_train)

model.predict(x_test)
y_pred = model.predict(x_test)
 

print(accuracy_score(y_test, y_pred))

pick = open('model.pickle', 'wb')
pickle.dump( {'model': model},pick)

pick.close()
