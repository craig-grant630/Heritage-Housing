import streamlit as st


def hypothesis_body():


    st.write("## 🔍 Project Hypothesis & Validation")


    st.markdown("### 🏠 Hypothesis 1: Bigger Homes Mean Higher Prices")
    st.success(
        "We believed that the **size of a home** would significantly impact "
        "its sale price.\n\n"
        "**✅ Confirmed:**\n"
        "- Strong positive correlation found between **Overall Quality (OverallQual)** "
        "and **SalePrice**.\n"
        "- Both **Pearson** and **Spearman** methods support this.\n\n"
        "💡 *Insight:* Higher-quality homes typically command higher prices."
    )


    st.markdown("### 🕒 Hypothesis 2: Newer Homes Sell for More")
    st.success(
        "We assumed that **newer properties** would have higher sale values.\n\n"
        "**✅ Confirmed:**\n"
        "- Moderate positive correlation between **YearBuilt** and **SalePrice**.\n"
        "- Newer homes generally sell for more according to **Pearson correlation**.\n\n"
        "💡 *Insight:* Age of the property plays a noticeable role in pricing."
    )


    st.markdown("### 🧱 Hypothesis 3: Better Build Quality Boosts Price")
    st.success(
        "We expected that **well-constructed homes** would fetch higher prices.\n\n"
        "**✅ Confirmed:**\n"
        "- Strong positive correlations with:\n"
        "  - **GrLivArea** (Above-ground living space)\n"
        "  - **GarageArea**\n"
        "  - **TotalBsmtSF** (Basement size)\n"
        "  - **1stFlrSF** (First floor area)\n\n"
        "💡 *Insight:* Larger and better-equipped homes drive value upward."
    )


    st.markdown("### 📊 Final Validation")
    st.info(
        "The **House Price Correlation Study** supports all three hypotheses.\n\n"
        "✅ Larger\n"
        "✅ Newer\n"
        "✅ Higher-quality\n\n"
        "🏡 *Homes with these attributes tend to sell for more in Ames, Iowa.*\n\n"
        "**Strategic Recommendation:**\n"
        "Clients should focus on improving size, condition, or features where possible "
        "to maximize the sale value of their properties."
    )
