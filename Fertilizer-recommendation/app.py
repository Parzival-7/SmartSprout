import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Datasets/Fertilizer_recommendation.csv")

# Encode categorical features
label_encoders = {}
categorical_cols = ['Soil Type', 'Crop Type', 'Fertilizer Name']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df.drop('Fertilizer Name', axis=1)
y = df['Fertilizer Name']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Streamlit App UI
st.title("🌾 Crop Fertilizer Recommendation System")

temp = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=100, value=25)
humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100, value=50)
nitrogen = st.number_input("🧪 Nitrogen (ppm)", min_value=0, max_value=500, value=100)
potassium = st.number_input("🧪 Potassium (ppm)", min_value=0, max_value=500, value=100)
phosphorous = st.number_input("🧪 Phosphorous (ppm)", min_value=0, max_value=500, value=100)
moisture = st.number_input("💦 Moisture (%)", min_value=0, max_value=100, value=30)
soil_type = st.selectbox("🪨 Select Soil Type", label_encoders['Soil Type'].classes_)
crop_type = st.selectbox("🌱 Select Crop Type", label_encoders['Crop Type'].classes_)

# Predict button
if st.button("Predict Fertilizer"):
    input_data = pd.DataFrame([[
    temp,
    humidity,
    moisture,
    label_encoders['Soil Type'].transform([soil_type])[0],
    label_encoders['Crop Type'].transform([crop_type])[0],
    nitrogen,
    potassium,
    phosphorous
]], columns=X.columns)

    pred = model.predict(input_data)
    fertilizer = label_encoders['Fertilizer Name'].inverse_transform(pred)[0]
    st.success(f"🧾 Recommended Fertilizer: **{fertilizer}**")
