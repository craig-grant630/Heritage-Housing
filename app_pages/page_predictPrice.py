import streamlit as st
import pandas as pd
from src.management import load_house_data, load_pkl_file, load_inherit_data
from src.predictive_analysis_ui import predict_sale_price


def house_predict_price_body():

    # Load necessary files
    version = 'v1'
    output_dir = "outputs/ml_pipeline/predict_saleprice"
    pipeline = load_pkl_file(f"{output_dir}/{version}/best_regressor_pipeline.pkl")
    best_features = pd.read_csv(f"{output_dir}/{version}/X_train.csv").columns.to_list()
    df_inherit = load_inherit_data()

    st.title("🏡 House Price Predictor")
    st.markdown("Use this tool to predict the sale price of houses in Ames, Iowa. \n"
    "🔍 Curious how the model makes its predictions? Explore the most important features and model performance on the Model Insights page.")

    st.subheader("📄 Inherited Houses: Predicted Prices")
    st.info("Below are the details and predicted sale prices for the four inherited properties.")
    st.dataframe(df_inherit)

    # Filter for features used in the model
    df_inherit_filtered = df_inherit.filter(best_features)
    predictions = pipeline.predict(df_inherit_filtered).round(0)
    df_inherit['Predicted Sale Price'] = predictions

    st.success(f"Total Predicted Sale Price of All Inherited Houses: **${int(predictions.sum()):,}**")
    st.dataframe(df_inherit[['Predicted Sale Price'] + best_features])

    st.markdown("---")
    st.subheader("📊 Predict Price for Any House in Ames")

    st.info("Use the sliders and inputs below to describe a house and click 'Predict Sale Price'.")

    X_live = DrawInputsWidgets(best_features)

#https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state assisted with the save predictions

    if "saved_predictions" not in st.session_state:
        st.session_state.saved_predictions = []

    house_label = st.text_input("Name this house entry (e.g., '3-bed remodel', 'Luxury build')")

    if st.button("➕ Save Prediction"):
        if not house_label:
            st.warning("⚠️ Please enter a name for this house.")
        else:
            X_input = X_live.copy()
            prediction = pipeline.predict(X_input[best_features])[0]
            X_input["Predicted Sale Price"] = round(prediction, 0)
            X_input["Label"] = house_label
            st.session_state.saved_predictions.append(X_input)

    if st.session_state.saved_predictions:
        st.subheader("🏘 Compare Saved Houses")
        df_compare = pd.concat(st.session_state.saved_predictions, ignore_index=True)
        st.dataframe(df_compare)

    if st.button("🧹 Clear Saved Houses"):
        st.session_state.saved_predictions = []

# Code adapted from Code instituts Churnometer Project
def DrawInputsWidgets(best_features):
    """Generates input widgets for selected features."""
    df = load_house_data()
    X_live = pd.DataFrame(index=[0])

    col_count = 3
    cols = st.columns(col_count)

    for idx, feature in enumerate(best_features):
        col = cols[idx % col_count]
        if pd.api.types.is_numeric_dtype(df[feature]):
            min_val = int(df[feature].min() * 0.4)
            max_val = int(df[feature].max() * 1.8)
            default_val = int(df[feature].median())
            value = col.number_input(
                label=feature,
                min_value=min_val,
                max_value=max_val,
                value=default_val,
                help=f"Enter a value for {feature}"
            )
        else:
            options = df[feature].unique().tolist()
            value = col.selectbox(feature, options, index=0)
        X_live[feature] = value

    return X_live
