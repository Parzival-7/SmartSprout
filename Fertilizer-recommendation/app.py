import streamlit as st
import pandas as pd

# Load dataset
try:
    df = pd.read_csv("Datasets/Fertilizer_recommendation.csv")
except FileNotFoundError:
    st.error("CSV file not found. Please check the path and filename.")
    st.stop()

# Check for required columns
required_columns = ['Crop Type', 'Fertilizer Name']
if not all(col in df.columns for col in required_columns):
    st.error("CSV file must contain 'Crop Type' and 'Fertilizer Name' columns.")
    st.stop()

# App title
st.title("🌱 Fertilizer Recommendation System")

# Crop selection
crops = df['Crop Type'].unique()
selected_crop = st.selectbox("Select a Crop", sorted(crops))

# Show fertilizers for selected crop
if selected_crop:
    st.subheader(f"Recommended Fertilizers for {selected_crop}")
    fertilizers = df[df['Crop Type'] == selected_crop]['Fertilizer Name'].unique()
    for fert in fertilizers:
        st.write(f"• {fert}")
