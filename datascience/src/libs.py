import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

def generate_data(rows=100, cols=5):
    df = pd.DataFrame(np.concatenate((np.random.normal(10, 1, (rows, cols)),
                                  np.random.binomial(1, 0.5, (rows, 1))), axis=1), 
                  columns=['col_'+str(m) for m in list(range(cols))]+['y'])
    return df

def print_generated_data(df):
    print(df)

def train_test_split(df, test_size=0.2):
    train = df.sample(frac=1-test_size)
    test = df.drop(train.index)
    return train, test

def train_model_and_return_auc(train,test, model):
    train_copy, test_copy = train.copy(), test.copy()
    y_train, y_test = train_copy.pop('y'), test_copy.pop('y')
    model.fit(train_copy, y_train)
    return roc_auc_score(y_test, model.predict(test_copy))

# create 5 classification models from sklearn
def create_models():
    return [LogisticRegression(max_iter=500), RandomForestClassifier(), GradientBoostingClassifier(), SVC(), KNeighborsClassifier()]

def train_models_and_return_aucs(train, test, models):
    aucs = []
    for model in models:
        aucs.append(train_model_and_return_auc(train, test, model))
    return models, aucs

def mean_auc(aucs):
    return np.mean(aucs)

# ====================================================================================================
# create a seperate block for titanic dataset
# ====================================================================================================
from data import download_data, remove_data
from sklearn.model_selection import train_test_split
def download_titanic_and_split_dataset():
    path = download_data()
    df = pd.read_csv('src/titanic.csv')
    remove_data(path)
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df = df.dropna()
    X = pd.get_dummies(df.drop('Survived', axis=1))
    y = df['Survived']
    return train_test_split(X, y, test_size=0.2)

def train_model_and_return_auc_titanic(model, data):
    (X_train, X_test, y_train, y_test) = data
    model.fit(X_train, y_train)
    return roc_auc_score(y_test, model.predict(X_test))
