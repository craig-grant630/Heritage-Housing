import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.management import load_house_data, load_pkl_file
from src.evaluation_pipeline import (
    regression_performance, regression_plots
)


def insight_sale_price_body():
    # Load pipeline components and performance assets
    version = 'v1'
    base_path = f"outputs/ml_pipeline/predict_saleprice/{version}"
    
    pipeline = load_pkl_file(f"{base_path}/best_regressor_pipeline.pkl")
    feature_importance_img = plt.imread(f"{base_path}/features_importance.png")
    
    X_train = pd.read_csv(f"{base_path}/X_train.csv")
    X_test = pd.read_csv(f"{base_path}/X_test.csv")
    y_train = pd.read_csv(f"{base_path}/y_train.csv")
    y_test = pd.read_csv(f"{base_path}/y_test.csv")

    
    st.info(
        "This page presents an overview of the machine learning pipeline used to predict "
        "house sale prices in Ames, Iowa."
    )

    st.markdown(
        """
        ### 🔍 Model Overview
        - The objective was to build a model capable of accurately predicting house sale prices.
        - Our performance target was an **R² score of at least 0.75** on both training and test sets.
        - After evaluating multiple algorithms, **ExtraTreesRegressor** was selected for its strong and consistent performance.
        - Final pipeline results:
            - **Train R² Score:** 1
            - **Test R² Score:** 0.856
        - This performance meets the client's accuracy requirements.
        """
    )
    
    st.divider()

    # Show the pipeline
    st.subheader("🧠 Trained ML Pipeline")
    st.write(pipeline)
    st.divider()

    # Show selected features and importance
    st.subheader("⭐ Model Features & Importance")
    st.markdown("These are the top features selected to train the final model:")
    st.write(X_train.columns.to_list())
    st.image(feature_importance_img, caption="Feature Importance Plot", use_container_width=True)
    st.divider()

    # Show performance metrics
    st.subheader("📊 Model Performance Metrics")
    regression_performance(
        X_train=X_train, y_train=y_train,
        X_test=X_test, y_test=y_test,
        pipeline=pipeline
    )
    st.divider()

    # Show regression plots
    st.subheader("📉 Actual vs Predicted Sale Price")
    st.markdown(
        "*The plots below illustrate the relationship between actual and predicted sale prices "
        "for both training and test datasets.*"
    )

    regression_plots(
        X_train=X_train, y_train=y_train,
        X_test=X_test, y_test=y_test,
        pipeline=pipeline, alpha_scatter=0.5
    )

    st.markdown(
        """
        **Interpretation:**
        - Blue dots represent the actual sale prices, while their horizontal position shows the predicted prices.
        - The red diagonal line represents perfect prediction accuracy (Predicted = Actual).
        - Most points closely follow this line, indicating strong predictive performance from the model.
        """
    )
