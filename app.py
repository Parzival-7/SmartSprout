import streamlit as st
import pandas as pd

# Load the uploaded dataset
df = pd.read_csv("Datasets/Fertilizer_recommendation.csv")

# App Title
st.title("Fertilizer Recommendation System")

# Crop selection
crops = df['Crop'].unique()
selected_crop = st.selectbox("Select a Crop", sorted(crops))

# Show available queries for the selected crop
queries = df[df['Crop'] == selected_crop]['query'].unique()
selected_query = st.selectbox("Select a Query", sorted(queries))

# Get recommendation
if st.button("Get Recommendation"):
    result = df[(df['Crop'] == selected_crop) & (df['query'] == selected_query)]['KCCAns'].values
    if result:
        st.success(f"🧪 Recommendation: {result[0]}")
    else:
        st.warning("No recommendation found for this combination.")
