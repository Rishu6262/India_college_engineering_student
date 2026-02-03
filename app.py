import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model & feature names
model = pickle.load(open("placement_model.pkl", "rb"))
feature_names = pickle.load(open("feature_names.pkl", "rb"))

st.title("🎓 Engineering Student Placement Prediction")

# ---- USER INPUT ----
input_dict = {
    'cgpa': st.number_input("CGPA", 0.0, 10.0, 7.1),
    'backlogs': st.number_input("Backlogs", 0, 10, 2),
    'internships_completed': st.number_input("Internships", 0, 10, 1),
    'coding_skill_rating': st.slider("Coding Skill", 1, 5, 3),
    'communication_skill_rating': st.slider("Communication Skill", 1, 5, 3),
    'aptitude_skill_rating': st.slider("Aptitude Skill", 1, 5, 3),
    'projects_completed': st.number_input("Projects", 0, 50, 18),
    'hackathons_participated': st.number_input("Hackathons", 0, 20, 1),
    'certifications_count': st.number_input("Certifications", 0, 20, 3),
    'attendance_percentage': st.slider("Attendance %", 0, 100, 75),
    'study_hours_per_day': st.slider("Study Hours", 0, 12, 4),
    'sleep_hours': st.slider("Sleep Hours", 0, 12, 7),
    'stress_level': st.slider("Stress Level", 1, 10, 5),
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# ---- ALIGN FEATURES ----
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[feature_names]

# ---- PREDICTION ----
if st.button("🔮 Predict Placement"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ Student is likely to be PLACED")
    else:
        st.error("❌ Student is likely to be NOT PLACED")
