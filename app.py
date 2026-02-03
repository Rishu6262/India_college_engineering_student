# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd

# # Load model & feature names
# model = pickle.load(open("placement_model.pkl", "rb"))
# feature_names = pickle.load(open("feature_names.pkl", "rb"))

# st.title("🎓 Engineering Student Placement Prediction")

# # ---- USER INPUT ----
# input_dict = {
#     'cgpa': st.number_input("CGPA", 0.0, 10.0, 7.1),
#     'backlogs': st.number_input("Backlogs", 0, 10, 2),
#     'internships_completed': st.number_input("Internships", 0, 10, 1),
#     'coding_skill_rating': st.slider("Coding Skill", 1, 5, 3),
#     'communication_skill_rating': st.slider("Communication Skill", 1, 5, 3),
#     'aptitude_skill_rating': st.slider("Aptitude Skill", 1, 5, 3),
#     'projects_completed': st.number_input("Projects", 0, 50, 18),
#     'hackathons_participated': st.number_input("Hackathons", 0, 20, 1),
#     'certifications_count': st.number_input("Certifications", 0, 20, 3),
#     'attendance_percentage': st.slider("Attendance %", 0, 100, 75),
#     'study_hours_per_day': st.slider("Study Hours", 0, 12, 4),
#     'sleep_hours': st.slider("Sleep Hours", 0, 12, 7),
#     'stress_level': st.slider("Stress Level", 1, 10, 5),
# }

# # Convert to DataFrame
# input_df = pd.DataFrame([input_dict])

# # ---- ALIGN FEATURES ----
# for col in feature_names:
#     if col not in input_df.columns:
#         input_df[col] = 0

# input_df = input_df[feature_names]

# # ---- PREDICTION ----
# if st.button("🔮 Predict Placement"):
#     prediction = model.predict(input_df)[0]

#     if prediction == 1:
#         st.success("✅ Student is likely to be PLACED")
#     else:
#         st.error("❌ Student is likely to be NOT PLACED")

import streamlit as st
import pickle
import pandas as pd

# ---------------- LOAD MODEL & FEATURES ----------------
model = pickle.load(open("placement_model.pkl", "rb"))
feature_names = pickle.load(open("feature_names.pkl", "rb"))

st.set_page_config(
    page_title="India colleges Engineering Student Placement Prediction",
    layout="centered"
)

st.title("India colleges 🎓 Engineering Student Placement Prediction")
st.write(
    "Predict whether a student will be **Placed** or **Not Placed** "
    "based on academic and skill details."
)

# ---------------- USER INPUT ----------------
input_dict = {
    "cgpa": st.number_input("CGPA", 0.0, 10.0, 7.1),
    "backlogs": st.number_input("Number of Backlogs", 0, 10, 0),
    "internships_completed": st.number_input("Internships Completed", 0, 10, 1),
    "projects_completed": st.number_input("Projects Completed", 0, 50, 3),
    "coding_skill_rating": st.slider("Coding Skill Rating (1–5)", 1, 5, 3),
    "communication_skill_rating": st.slider("Communication Skill Rating (1–5)", 1, 5, 3),
    "aptitude_skill_rating": st.slider("Aptitude Skill Rating (1–5)", 1, 5, 3),
    "hackathons_participated": st.number_input("Hackathons Participated", 0, 20, 0),
    "certifications_count": st.number_input("Certifications Count", 0, 20, 1),
    "attendance_percentage": st.slider("Attendance Percentage", 0, 100, 75),
    "study_hours_per_day": st.slider("Study Hours Per Day", 0, 12, 4),
    "sleep_hours": st.slider("Sleep Hours", 0, 12, 7),
    "stress_level": st.slider("Stress Level (1–10)", 1, 10, 5),
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# ---------------- FEATURE ALIGNMENT ----------------
# Add missing columns as 0
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = 0

# Ensure same order as training
input_df = input_df[feature_names]

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Placement"):
    # Probabilities
    proba = model.predict_proba(input_df)[0]
    classes = model.classes_

    placed_prob = 0
    not_placed_prob = 0

    for i, cls in enumerate(classes):
        if cls == 1:
            placed_prob = proba[i] * 100
        else:
            not_placed_prob = proba[i] * 100

    st.subheader("📊 Prediction Confidence")
    st.write(f"✅ Placed Probability: **{placed_prob:.2f}%**")
    st.write(f"❌ Not Placed Probability: **{not_placed_prob:.2f}%**")

    THRESHOLD = 40  # realistic threshold for imbalance

    if placed_prob >= THRESHOLD:
        st.success("🎉 Student is likely to be **PLACED**")
    else:
        st.error("⚠️ Student is likely to be **NOT PLACED**")

st.markdown("---")
st.caption("⚠️ Prediction is based on historical data and machine learning models.")


