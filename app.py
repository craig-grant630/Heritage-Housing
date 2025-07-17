import streamlit as st

from app_pages.multi_page import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import hypothesis_body
from app_pages.page_housePrice_study import house_price_study_body
from app_pages.page_predictPrice import house_predict_price_body

app = MultiPage(app_name="Heritage Housing - SalePrice Predictor")

app.add_page("Project Summary", page_summary_body)
app.add_page("Hypothesis and Validation", hypothesis_body)
app.add_page("Sale Price Study", house_price_study_body)
app.add_page("Prediction of House Prices", house_predict_price_body)

app.run() 