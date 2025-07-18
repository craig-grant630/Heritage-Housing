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


def regression_plots(X_train, y_train, X_test, y_test, pipeline, alpha_scatter=0.5):
    """Generate scatter plots comparing actual vs predicted values for train and test sets."""

    # Generate predictions
    pred_train = pipeline.predict(X_train)
    pred_test = pipeline.predict(X_test)

    # Setup subplots
    fig, axes = plt.subplots(ncols=2, figsize=(14, 6), sharey=True)
    fig.suptitle("Predicted vs Actual Sale Prices", fontsize=16)

    # Train set plot
    sns.scatterplot(
        x=y_train.values.ravel(), y=pred_train,
        alpha=alpha_scatter, ax=axes[0], color="steelblue"
    )
    sns.lineplot(
        x=y_train.values.ravel(), y=y_train.values.ravel(),
        color='red', ax=axes[0], label="Ideal Fit"
    )
    axes[0].set_title("Training Set")
    axes[0].set_xlabel("Actual Sale Price")
    axes[0].set_ylabel("Predicted Sale Price")

    # Test set plot
    sns.scatterplot(
        x=y_test.values.ravel(), y=pred_test,
        alpha=alpha_scatter, ax=axes[1], color="steelblue"
    )
    sns.lineplot(
        x=y_test.values.ravel(), y=y_test.values.ravel(),
        color='red', ax=axes[1], label="Ideal Fit"
    )
    axes[1].set_title("Test Set")
    axes[1].set_xlabel("Actual Sale Price")
    axes[1].set_ylabel("Predicted Sale Price")

    # Improve layout
    for ax in axes:
        ax.legend()
        ax.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    st.pyplot(fig)
