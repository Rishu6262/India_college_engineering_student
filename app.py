import streamlit as st
import pickle
import numpy as np

# ---------------- LOAD MODEL ----------------
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Student Placement Prediction",
    layout="centered"
)

st.title("🎓 Engineering Student Placement Prediction")
st.write("Predict whether a student will be **Placed** or **Not Placed** based on academic and skill details.")

# ---------------- INPUT FIELDS ----------------
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
backlogs = st.number_input("Number of Backlogs", min_value=0, step=1)
internships = st.number_input("Internships Completed", min_value=0, step=1)

coding_skill = st.slider("Coding Skill Rating (1–5)", 1, 5, 3)
communication_skill = st.slider("Communication Skill Rating (1–5)", 1, 5, 3)
aptitude_skill = st.slider("Aptitude Skill Rating (1–5)", 1, 5, 3)

projects = st.number_input("Projects Completed", min_value=0, step=1)
hackathons = st.number_input("Hackathons Participated", min_value=0, step=1)
certifications = st.number_input("Certifications Count", min_value=0, step=1)

attendance = st.slider("Attendance Percentage", 0, 100, 75)
study_hours = st.slider("Study Hours Per Day", 0, 12, 4)

sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
stress_level = st.slider("Stress Level (1–10)", 1, 10, 5)

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Placement"):
    input_data = np.array([[cgpa, backlogs, internships,
                            coding_skill, communication_skill, aptitude_skill,
                            projects, hackathons, certifications,
                            attendance, study_hours, sleep_hours, stress_level]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Student is likely to be **PLACED**")
    else:
        st.error("❌ Student is likely to be **NOT PLACED**")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("📌 *This prediction is based on machine learning and may not reflect real-world outcomes.*")
