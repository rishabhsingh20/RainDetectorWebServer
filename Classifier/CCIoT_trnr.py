import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
#from sklearn import svm,preprocessing
from sklearn.externals import joblib
#from sklearn.linear_model import LogisticRegression as LR
#from sklearn.neighbors import KNeighborsClassifier as KNN
#from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier as BC
#from sklearn.ensemble import GradientBoostingClassifier as GB
#from sklearn.naive_bayes import GaussianNB as GN
#from sklearn.linear_model import LinearRegression as LiR


df = pd.read_csv('data1.csv')
X = np.array(df.drop(['Rainfall'],1))
y = np.array(df['Rainfall'])

X_train,X_test,y_train,y_test = tts(X,y,test_size=0.75)
#X_train = preprocessing.scale(X_train)
#X_test = preprocessing.scale(X_test)

#as of now winner = SVM

#clf = svm.SVC(gamma='auto',kernel='rbf',probability=True,decision_function_shape='ovr')
#clf.fit(X_train,y_train)
#print(clf.score(X_test,y_test))


#clf1 = LR(penalty='l2',solver='lbfgs',intercept_scaling=1,n_jobs=-1,max_iter=1e9,warm_start=True)
#clf1.fit(X_train,y_train)
#print(clf1.score(X_test,y_test))

#clf2 = KNN()
#clf2.fit(X_train,y_train)
#print(clf2.score(X_test,y_test))

#clf3 = RandomForestClassifier(n_estimators=100,criterion='gini',max_features='sqrt',warm_start=True)
#clf3.fit(X_train,y_train)
#print(clf3.score(X_test,y_test))

clf4 = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf4.fit(X_train,y_train)
#print(clf4.score(X_test,y_test))

clf5 = BC(clf4,n_estimators=100,max_samples=0.8,random_state=1)
clf5.fit(X_train,y_train)
print(clf5.score(X_test,y_test))

#clf6 = GB(n_estimators=100, learning_rate=0.1, max_features=2, max_depth=2, random_state=1)
#clf6.fit(X_train,y_train)
#print(clf6.score(X_test,y_test))

#clf7 = GN(var_smoothing=1e-3)
#clf7.fit(X_train,y_train)
#print(clf7.score(X_test,y_test))

#clf8 = LiR()
#clf8.fit(X_train,y_train)
#print(clf8.score(X_test,y_test))

joblib.dump(clf5, 'final_clf.pkl')

