#import pandas as pd
#import numpy as np
#from sklearn.model_selection import train_test_split as tts
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import BaggingClassifier as BC
from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)
from sklearn.externals import joblib
import pickle

#df = pd.read_csv('data1.csv')
#X = np.array(df.drop(['Rainfall'],1))
#y = np.array(df['Rainfall'])
#X_train,X_test,y_train,y_test = tts(X,y,test_size=1)
#clf = pickle.load(open('meh_good_enough.sav', 'rb'))
#clf4 = DecisionTreeClassifier(criterion='entropy',random_state=1)
#clf4.fit(X_train,y_train)
#clf5 = BC(clf4,n_estimators=100,max_samples=0.8,random_state=1)
#clf5.fit(X_train,y_train)

#temp = 23.00
#humid = 98.00

#html needs to be stored in a folder called templates
#@app.route('/')
#def index():
 #   return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def input():
    if request.method == 'POST':
        temp = request.form.get('temperature')
        humid = request.form.get('humidity')
        fin = [[temp,humid]]
        clf = joblib.load('pickle1.sav')
        pred = clf.predict(fin[0:1])
        ans = pred[0]
        print(ans)
        if ans == 0:
            flag = 0
        else:
            flag = 1
        if flag == 0:
            return '<h1>It wont rain</h1>'
        else:
            return '</h1>It will rain</h1>'
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug = True)

