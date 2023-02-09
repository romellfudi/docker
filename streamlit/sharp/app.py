import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

st.write(
    """
# Boston House Price Prediction App

This app predicts the **Boston House Price**!
"""
)
st.write("---")

# Loads the Boston House Price Dataset
boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
Y = pd.DataFrame(boston.target, columns=["MEDV"])

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header("Specify Input Parameters")


def user_input_features():
    CRIM = st.sidebar.slider(
        "CRIM", X.CRIM.min().item(), X.CRIM.max().item(), X.CRIM.mean().item()
    )
    ZN = st.sidebar.slider(
        "ZN", X.ZN.min().item(), X.ZN.max().item(), X.ZN.mean().item()
    )
    INDUS = st.sidebar.slider(
        "INDUS", X.INDUS.min().item(), X.INDUS.max().item(), X.INDUS.mean().item()
    )
    CHAS = st.sidebar.slider(
        "CHAS", X.CHAS.min().item(), X.CHAS.max().item(), X.CHAS.mean().item()
    )
    NOX = st.sidebar.slider(
        "NOX", X.NOX.min().item(), X.NOX.max().item(), X.NOX.mean().item()
    )
    RM = st.sidebar.slider(
        "RM", X.RM.min().item(), X.RM.max().item(), X.RM.mean().item()
    )
    AGE = st.sidebar.slider(
        "AGE", X.AGE.min().item(), X.AGE.max().item(), X.AGE.mean().item()
    )
    DIS = st.sidebar.slider(
        "DIS", X.DIS.min().item(), X.DIS.max().item(), X.DIS.mean().item()
    )
    RAD = st.sidebar.slider(
        "RAD", X.RAD.min().item(), X.RAD.max().item(), X.RAD.mean().item()
    )
    TAX = st.sidebar.slider(
        "TAX", X.TAX.min().item(), X.TAX.max().item(), X.TAX.mean().item()
    )
    PTRATIO = st.sidebar.slider(
        "PTRATIO",
        X.PTRATIO.min().item(),
        X.PTRATIO.max().item(),
        X.PTRATIO.mean().item(),
    )
    B = st.sidebar.slider("B", X.B.min().item(), X.B.max().item(), X.B.mean().item())
    LSTAT = st.sidebar.slider(
        "LSTAT", X.LSTAT.min().item(), X.LSTAT.max().item(), X.LSTAT.mean().item()
    )
    data = {
        "CRIM": CRIM,
        "ZN": ZN,
        "INDUS": INDUS,
        "CHAS": CHAS,
        "NOX": NOX,
        "RM": RM,
        "AGE": AGE,
        "DIS": DIS,
        "RAD": RAD,
        "TAX": TAX,
        "PTRATIO": PTRATIO,
        "B": B,
        "LSTAT": LSTAT,
    }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

# Main Panel

# Print specified input parameters
st.header("Specified Input parameters")
st.write(df)
st.write("---")

# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)
# Apply Model to Make Prediction
prediction = model.predict(df)

st.header("Prediction of MEDV")
st.write(prediction)
st.write("---")

# Explaining the model's predictions using SHAP values
# https://github.com/slundberg/shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.set_option("deprecation.showPyplotGlobalUse", False)

st.header("Feature Importance")
plt.title("Feature importance based on SHAP values")
shap.summary_plot(shap_values, X)
st.pyplot(bbox_inches="tight")
st.write("---")

plt.title("Feature importance based on SHAP values (Bar)")
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(bbox_inches="tight")
