import streamlit as st
import pandas as pd

# Load dataset safely
try:
    df = pd.read_csv("Datasets/Fertilizer_recommendation.csv")
except FileNotFoundError:
    st.error("Dataset file not found. Please check the path.")
    st.stop()

# Required columns check
required_columns = ['Crop Type', 'Fertilizer Name', 'query', 'KCCAns']
if not all(col in df.columns for col in required_columns):
    st.error("CSV file is missing required columns: 'Crop Type', 'Fertilizer Name', 'query', or 'KCCAns'")
    st.stop()

# App Title
st.title("Fertilizer Recommendation System")

# Crop selection
crops = df["Crop Type"].unique()
selected_crop = st.selectbox("Select Crop", sorted(crops))

# Show available queries for the selected crop
queries = df[df['Crop Type'] == selected_crop]['query'].unique()
selected_query = st.selectbox("Select a Query", sorted(queries))

# Get recommendation
if st.button("Get Recommendation"):
    result = df[(df['Crop Type'] == selected_crop) & (df['query'] == selected_query)]['KCCAns'].values
    if result:
        st.success(f"🧪 Recommendation: {result[0]}")
    else:
        st.warning("No recommendation found for this combination.")
