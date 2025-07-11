import streamlit as st


def page_summary_body():


    st.info(
        "The Ames Housing Prices dataset, available on Kaggle, "
        "contains detailed information on residential properties in "
        "Ames, Iowa. It includes approximately 1,460 records of homes "
        "with a variety of features describing the physical "
        "characteristics of each house such as living area, basement "
        "details, garage information, kitchen quality, lot size, porch "
        "and deck areas, as well as construction and remodeling years. "
        "The dataset also provides the sale price for each property, "
        "making it ideal for exploring relationships between house "
        "attributes and market value or for building predictive models. "
        "This comprehensive dataset is widely used for regression and "
        "housing market analysis tasks."
    )


    st.success(
        "### Business Requirements\n"
        "The project is guided by two main business objectives:\n"
        "1. **Correlation Analysis:** To identify and visualize how "
        "various house attributes relate to the sale price.\n"
        "2. **Sale Price Prediction:** To develop a predictive model "
        "for estimating the sale price of the client's four inherited "
        "houses and any other property in Ames, Iowa."
    )


    st.markdown(
        "### Documentation\n"
        "For a comprehensive understanding of the project and dataset, "
        "please refer to the "
        "[Project README](https://github.com/craig-grant630/"
        "Heritage-Housing/blob/main/README.md)."
    )
