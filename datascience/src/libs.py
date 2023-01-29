import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

def generate_data(n):
    return pd.DataFrame({'x': np.random.normal(size=n),
                         'y': [np.random.randint(0, 2) for _ in range(n)]})

def print_generated_data(df):
    print(df)

def train_test_split(df, test_size=0.2):
    train = df.sample(frac=1-test_size)
    test = df.drop(train.index)
    return train, test

def train_model_and_return_auc(train,test, model):
    model.fit(train[['x']], train['y'])
    return roc_auc_score(test['y'], model.predict(test[['x']]))

# create 5 classification models from sklearn
def create_models():
    return [LogisticRegression(), RandomForestClassifier(), GradientBoostingClassifier(), SVC(), KNeighborsClassifier()]

def train_models_and_return_aucs(train, test, models):
    aucs = []
    for model in models:
        aucs.append(train_model_and_return_auc(train, test, model))
    return aucs

def mean_auc(aucs):
    return np.mean(aucs)

