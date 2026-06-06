# 🎓 Indian Engineering Student Placement Prediction

## 📌 Project Overview

The **Indian Engineering Student Placement Prediction System** is a Machine Learning project designed to analyze student academic performance, technical skills, internships, projects, certifications, and other career-related factors to predict placement outcomes.

The project helps students understand which factors significantly impact placement opportunities and provides a data-driven approach to career preparation.

This dataset contains information about **5000 engineering students** from different branches and backgrounds across India.

---

# 🚀 Objectives

* Predict student placement chances using Machine Learning.
* Analyze factors affecting placements.
* Compare multiple ML algorithms.
* Identify the best-performing model.
* Provide insights for students to improve employability.

---

# 📊 Dataset Information

### Dataset Name

**Indian Engineering Student Placement Dataset**

### Total Records

* 5000 Students

### Total Features

* 23 Features

---

## Features Description

| Feature                     | Description                 |
| --------------------------- | --------------------------- |
| Student_ID                  | Unique Student ID           |
| gender                      | Male/Female                 |
| branch                      | Engineering Branch          |
| cgpa                        | College CGPA                |
| tenth_percentage            | Class 10 Percentage         |
| twelfth_percentage          | Class 12 Percentage         |
| backlogs                    | Number of Backlogs          |
| study_hours_per_day         | Daily Study Hours           |
| attendance_percentage       | Attendance Percentage       |
| projects_completed          | Number of Projects          |
| internships_completed       | Number of Internships       |
| coding_skill_rating         | Coding Skills Rating        |
| communication_skill_rating  | Communication Skills Rating |
| aptitude_skill_rating       | Aptitude Skills Rating      |
| hackathons_participated     | Number of Hackathons        |
| certifications_count        | Number of Certifications    |
| sleep_hours                 | Daily Sleep Hours           |
| stress_level                | Stress Level                |
| part_time_job               | Yes/No                      |
| family_income_level         | Income Category             |
| city_tier                   | Tier 1 / Tier 2 / Tier 3    |
| internet_access             | Yes/No                      |
| extracurricular_involvement | High / Medium / Low         |

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

# 📂 Project Structure

```bash
Placement_Prediction_Project/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── encoder.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── indian_engineering_student_placement.csv
│
├── notebooks/
│   └── placement_prediction.ipynb
│
└── assets/
    └── screenshots
```

---

# 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

### Academic Analysis

* CGPA Distribution
* 10th Percentage Analysis
* 12th Percentage Analysis
* Attendance Impact

### Skill Analysis

* Coding Skills
* Communication Skills
* Aptitude Skills

### Career Analysis

* Internships
* Projects
* Certifications
* Hackathons

### Demographic Analysis

* Gender Distribution
* Branch-wise Distribution
* City Tier Comparison

### Lifestyle Analysis

* Stress Levels
* Sleep Hours
* Study Hours

---

# 🤖 Machine Learning Models Used

Multiple machine learning algorithms were trained and compared.

## 1. Logistic Regression

Advantages:

* Fast Training
* Easy Interpretation
* Good Baseline Model

---

## 2. Decision Tree

Advantages:

* Handles Nonlinear Relationships
* Easy Visualization
* Feature Importance Analysis

---

## 3. Random Forest

Advantages:

* High Accuracy
* Reduces Overfitting
* Robust Predictions

---

## 4. K-Nearest Neighbors (KNN)

Advantages:

* Simple and Easy to Implement
* Effective for Classification Tasks
* Makes Predictions Based on Similar Data Points
* Performs Well with Properly Scaled Data

---

# 🏆 Best Model Selection

All models were trained and evaluated.

The best model was selected based on:

* Highest Accuracy
* Better Precision
* Better Recall
* Better Generalization

Possible top-performing models:

* Random Forest
* K-Nearest Neighbors (KNN)

depending on train-test split results.

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

```

# ⚙️ Data Preprocessing

The following preprocessing steps were applied:

### Missing Value Handling

* Checked for null values
* Cleaned inconsistent records

### Encoding

Categorical features converted using:

* Label Encoding
* One-Hot Encoding

### Feature Scaling

Applied:

```python
StandardScaler()
```

for numerical features.

---

# 📈 Model Evaluation Metrics

Models were evaluated using:

### Accuracy

```python
accuracy_score()
```

### Precision

```python
precision_score()
```

### Recall

```python
recall_score()
```

### F1 Score

```python
f1_score()
```

### Confusion Matrix

```python
confusion_matrix()
```

---

# 🏆 Best Model Selection

All models were trained and evaluated.

The best model was selected based on:

* Highest Accuracy
* Better Precision
* Better Recall
* Better Generalization

Possible top-performing models:

* KNN
* Decsion Tree

depending on train-test split results.

---

# 📊 Important Placement Factors

The following features significantly influence placement chances:

1. CGPA
2. Coding Skill Rating
3. Communication Skills
4. Internships Completed
5. Projects Completed
6. Certifications Count
7. Aptitude Skills
8. Attendance Percentage
9. Hackathon Participation
10. Branch

---

# 💻 Streamlit Web Application

A user-friendly Streamlit application was developed where users can:

### Input Student Details

* CGPA
* Skills
* Internships
* Projects
* Certifications
* Attendance
* Communication Skills
* Aptitude Skills

### Get Prediction

The application predicts:

* Placement Probability
* Placement Status

in real-time.

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

---

# Future Improvements

* Deep Learning Models
* Placement Probability Score
* Resume Analysis Module
* Interview Readiness Assessment
* Personalized Career Recommendations
* College-wise Placement Insights

---

# Learning Outcomes

Through this project, I learned:

* Data Cleaning
* Feature Engineering
* Data Visualization
* Machine Learning Algorithms
* Model Evaluation
* Hyperparameter Tuning
* Streamlit Deployment
* End-to-End ML Workflow

---

## Author

**Rishu Gurjar**

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer

Connect with me on LinkedIn and GitHub to explore more Machine Learning and Data Science projects.

---

📜 Disclaimer

This project is developed for educational, research, and learning purposes only.

The placement predictions generated by this system are based on machine learning algorithms trained on historical student data. The results are intended to provide insights and demonstrate the application of data science and machine learning techniques in placement prediction.

Prediction outcomes should not be considered as guaranteed placement decisions, official recruitment evaluations, or career advice. Actual placement results may vary depending on factors such as interview performance, technical skills, communication abilities, market conditions, and company-specific hiring criteria.

The author is not responsible for any decisions made based on the predictions generated by this application.

---

# Conclusion

This project demonstrates how Machine Learning can help predict engineering student placement opportunities by analyzing academic, technical, and personal development factors. By comparing multiple algorithms such as Logistic Regression, Decision Tree, Random Forest, KNN, the system identifies the most effective model and provides meaningful insights into student employability.

---
