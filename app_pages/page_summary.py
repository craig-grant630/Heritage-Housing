import streamlit as st


def page_summary_body():


    st.info(
        
        "The Ames Housing Prices dataset, available on Kaggle, contains detailed information on residential properties in Ames, Iowa. " 
        "It includes approximately 1,460 records of homes with a variety of features describing the physical characteristics of each house "
        "such as living area, basement details, garage information, kitchen quality, lot size, porch and deck areas, as well as construction " 
        "and remodeling years. The dataset also provides the sale price for each property, making it ideal for exploring relationships between " 
        "house attributes and market value or for building predictive models. This comprehensive dataset is widely used for regression and housing market analysis tasks."
        
    )   

    st.success(
        "### Business Requirements\n"
        "The project is guided by two main business objectives:\n"
        "1. **Correlation Analysis:** To identify and visualize how various house attributes relate to the sale price.\n"
        "2. **Sale Price Prediction:** To develop a predictive model for estimating the sale price of the client's four inherited houses and any other property in Ames, Iowa."
    )

    st.markdown(
        "### Documentation\n"
        "For a comprehensive understanding of the project and dataset, please refer to the "
        "[Project README](https://github.com/craig-grant630/Heritage-Housing/blob/main/README.md)."
    )

    st.markdown(
        """
        ### Dataset Variables

        | Variable      | Meaning                                                      | Units / Range                                      |
        |--------------:|-------------------------------------------------------------|---------------------------------------------------|
        | 1stFlrSF      | First Floor square feet                                      | 334 - 4692 Sq. ft.                                |
        | 2ndFlrSF      | Second floor square feet                                     | 0 - 2065 Sq. ft.                                  |
        | BedroomAbvGr  | Bedrooms above grade (excludes basement bedrooms)           | 0 - 8 Bedrooms                                    |
        | BsmtExposure  | Refers to walkout or garden level walls                     | Gd: Good; Av: Average; Mn: Minimum; No: None     |
        | BsmtFinType1  | Rating of basement finished area                             | GLQ, ALQ, BLQ, Rec, LwQ, Unf, None                |
        | BsmtFinSF1    | Type 1 finished square feet                                  | 0 - 5644 Sq. ft.                                  |
        | BsmtUnfSF     | Unfinished square feet of basement area                      | 0 - 2336 Sq. ft.                                  |
        | TotalBsmtSF   | Total square feet of basement area                           | 0 - 6110 Sq. ft.                                  |
        | GarageArea    | Size of garage in square feet                                | 0 - 1418 Sq. ft.                                  |
        | GarageFinish  | Interior finish of the garage                                | Fin: Finished; RFn: Rough Finished; Unf; None    |
        | GarageYrBlt   | Year garage was built                                        | 1900 - 2010                                       |
        | GrLivArea     | Above grade (ground) living area square feet                 | 334 - 5642 Sq. ft.                                |
        | KitchenQual   | Kitchen quality                                             | Ex: Excellent; Gd: Good; TA: Typical; Fa: Fair; Po: Poor |
        | LotArea       | Lot size in square feet                                      | 1300 - 215245 Sq. ft.                             |
        | LotFrontage   | Linear feet of street connected to property                  | 21 - 313 Linear ft.                               |
        | MasVnrArea    | Masonry veneer area in square feet                           | 0 - 1600 Sq. ft.                                  |
        | EnclosedPorch | Enclosed porch area in square feet                           | 0 - 286 Sq. ft.                                   |
        | OpenPorchSF   | Open porch area in square feet                               | 0 - 547 Sq. ft.                                   |
        | OverallCond   | Rates the overall condition of the house                     | 10 (Very Excellent) to 1 (Very Poor)              |
        | OverallQual   | Rates the overall material and finish of the house           | 10 (Very Excellent) to 1 (Very Poor)              |S
        | WoodDeckSF    | Wood deck area in square feet                                | 0 - 736 Sq. ft.                                   |
        | YearBuilt     | Original construction date                                   | 1872 - 2010                                       |
        | YearRemodAdd  | Remodel date (same if no remodeling or additions)            | 1950 - 2010                                       |
        | SalePrice     | Sale Price                                                  | $34,900 - $755,000                                |
        """
    )
