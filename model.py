import sklearn
import pandas as pd
import numpy as np

Data1= pd.read_csv('FINALFINALFINALRISK.csv')
Data1 = Data1.drop('race', axis = 1)
Data1 = Data1.drop('training', axis = 1)
Data1 = Data1.drop('count', axis = 1)

from sklearn.model_selection import train_test_split

X = Data1.drop('cancer', axis = 1)
y = Data1['cancer']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=42)

# class_weight = ({0:1,1:1000})

# import imblearn
# from collections import Counter
# from imblearn.over_sampling import RandomOverSampler

# os = RandomOverSampler(sampling_strategy = 0.78)

# X_train_os,y_train_os = os.fit_resample(X_train,y_train)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression(random_state = 0)
logmodel.fit(X_train,y_train)
y_pred_Log = logmodel.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# View accuracy score
log = round(accuracy_score(y_test, y_pred_Log),2)*100
print(str(log)+'%')

# View confusion matrix for test data and predictions
print(confusion_matrix(y_test, y_pred_Log))

# View the classification report for test data and predictions
print(classification_report(y_test, y_pred_Log))

import pickle
pickle.dump (logmodel, open ("logistic_regression.sav", "wb"))