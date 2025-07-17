import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from src.management import load_house_data

sns.set_style("whitegrid")

def house_price_study_body():

    # Load dataset
    df = load_house_data()

    # Key variables to analyze
    core_vars = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    # Business Requirement
    with st.expander("📌 Business Requirement 1"):
        st.markdown("""
        The client wants to understand **how different property features affect 
        the sale price** of houses. This analysis aims to explore those 
        relationships through correlation with visualization.
        """)

    # Dataset preview
    with st.expander("🔍 Preview the Dataset"):
        st.markdown(f"* Dataset contains `{df.shape[0]}` rows and `{df.shape[1]}` columns.")
        st.dataframe(df.head(10), use_container_width=True)

    st.divider()

    # Correlation Study Introduction
    st.subheader("📈 Correlation Study")
    st.markdown("""  
        To better understand the relationship between various features and 
        house sale price, correlation analyses were conducted using both the 
        Pearson and Spearman methods. These studies aimed to identify which 
        variables are most strongly associated with sale price. The results 
        highlighted several features that showed the strongest positive 
        correlations with sale price:
        """)
    
    st.markdown(f"**Key Variables:** `{', '.join(core_vars)}`")

    with st.expander("📋 Study Summary & Findings"):
        st.info("""
        - **Overall Quality** had the strongest correlation with sale price.
        - **Total Basement SF** and **Garage Area** followed closely.
        - **First Floor SF** and **Above Ground Living Area** also had high 
        positive correlations.
        - **Year Built** showed a moderate positive correlation, making it the 
        weakest among the top six.
        """)

    st.divider()

    # Prepare data for EDA
    df_eda = df[core_vars + ['SalePrice']]

    # Regression Plots
    if st.checkbox("📊 Show Regression Plots (Feature vs. Sale Price)"):
        st.markdown("Visualizing how each feature affects the Sale Price.")

        def plot_regress(df, col, target):
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.regplot(data=df, x=col, y=target, line_kws={"color": "red"})
            plt.title(f"{col} vs. {target}", fontsize=16)
            st.pyplot(fig)

        for feature in df_eda.drop('SalePrice', axis=1).columns:
            plot_regress(df_eda, feature, 'SalePrice')

    st.success("""
    ### 🏁 Summary of Key Findings
    - All six selected variables show a positive correlation with SalePrice, 
    indicating that as their values increase, the sale price of the properties 
    tends to increase as well. This suggests these features are meaningful 
    drivers of property value.

    - Among these variables, YearBuilt has the least impact on SalePrice. 
    This could imply that while the age of a house matters, other factors have 
    a stronger influence on pricing in this dataset.

    - TotalBsmtSF (Total Basement Square Footage) emerges as the most 
    important predictor, highlighting that larger basement areas significantly 
    contribute to higher sale prices. This aligns with the intuition that 
    additional living or storage space adds value.

    - The remaining variables—such as 1stFlrSF, GarageArea, GrLivArea, and 
    OverallQual—also show strong positive relationships with SalePrice, 
    reinforcing their relevance as key factors in determining home value.
    """)

