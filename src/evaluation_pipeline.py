import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# Evaluate the performance of a regression model on train and test sets
def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    st.write("**Model Evaluation**")
    st.write("* **Train Set**")
    regression_evaluation(X_train, y_train, pipeline)
    st.write("* **Test Set**")
    regression_evaluation(X_test, y_test, pipeline)


def regression_evaluation(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write(
        'R2 Score:', r2_score(y, prediction).round(3))
    st.write(
        'Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))
    st.write(
        'Mean Squared Error:', mean_squared_error(y, prediction).round(3))
    st.write(
        'Root Mean Squared Error:', np.sqrt(
            mean_squared_error(y, prediction)).round(3))
    st.write("\n")


#