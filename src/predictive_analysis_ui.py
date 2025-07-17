import streamlit as st

#Adapted from Code Institutes Walkthrough Project
def predict_sale_price(X_live, best_features, pipeline):
    """
    Predicts the house sale price using the trained ML pipeline and user-provided input.
    
    Parameters:
    - X_live (DataFrame): User input data (1 row)
    - best_features (list): List of features used by the pipeline
    - pipeline (sklearn Pipeline): Trained regression pipeline

    Displays:
    - Predicted sale price in a formatted Streamlit success box
    """

    try:
        # Ensure all required features are present
        missing_features = [feat for feat in best_features if feat not in X_live.columns]
        if missing_features:
            st.warning(f"Missing required input features: {missing_features}")
            return

        # Subset to only required features
        X_input = X_live[best_features]

        # Make prediction
        prediction = pipeline.predict(X_input)[0]
        sale_price = f"${prediction:,.0f}"

        # Display result
        st.success(
            f"✅ The predicted sale price for the house is: **{sale_price}**"
        )

    except Exception as e:
        st.error(f"🚫 Prediction failed due to an error:\n\n{str(e)}")