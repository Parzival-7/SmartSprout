import streamlit as st
import pandas as pd

# Load the uploaded dataset once
try:
    df = pd.read_csv("Datasets/Fertilizer_recommendation.csv")
except FileNotFoundError:
    st.error("Dataset not found at Datasets/Fertilizer_recommendation.csv")
    st.stop()

# App Title
st.title("🌾 Fertilizer Recommendation System")

# Crop selection
if "Crop Type" not in df.columns or "Fertilizer Name" not in df.columns or "KCCAns" not in df.columns:
    st.error("CSV file is missing required columns: 'Crop Type', 'Fertilizer Name', or 'KCCAns'")
    st.stop()

crops = sorted(df["Crop Type"].unique())
selected_crop = st.select_
