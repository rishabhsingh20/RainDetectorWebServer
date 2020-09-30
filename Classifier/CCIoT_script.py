import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn import svm,preprocessing
from sklearn.externals import joblib

clf = joblib.load('final_clf.pkl')

df = pd.read_csv('data1.csv')
X = np.array(df.drop(['Rainfall'],1))
y = np.array(df['Rainfall'])

prediction = clf.predict(X[0:50])
print(prediction)
