import streamlit as st

from app_pages.multi_page import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import hypothesis_body

app = MultiPage(app_name="Heritage Housing - SalePrice Predictor")

app.add_page("Project Summary", page_summary_body)
app.add_page("Hypothesis and Validation", hypothesis_body)

app.run() 