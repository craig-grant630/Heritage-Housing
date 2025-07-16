import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache_data
def load_house_data():
    df = pd.read_csv("outputs/datasets/collection/HousePrices.csv")
    return df

