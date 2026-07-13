# 🎓 Indian Engineering Student Placement Prediction

---

🚀 Live Demo

🌐 Streamlit Application:
https://indiacollegeengineeringstudent-wgmnzas9bh3aszqqfyjyx9.streamlit.app/

---

# 📌 Project Overview

The **Indian Engineering Student Placement Prediction System** is an end-to-end **Machine Learning** project developed to predict the placement status of engineering students based on their academic performance, technical skills, internships, projects, certifications, and other career-related attributes. The project applies data preprocessing, exploratory data analysis (EDA), feature engineering, and multiple classification algorithms to identify the key factors that influence placement outcomes.

The dataset consists of **5,000 engineering student records** collected from various engineering branches across India. It includes academic achievements, technical competencies, extracurricular activities, and demographic information, providing a comprehensive view of student profiles.

The primary objective of this project is to build a predictive model that can estimate a student's placement probability with high accuracy. The trained model is deployed using **Streamlit**, allowing users to enter student information through an interactive web interface and receive real-time placement predictions.

This project demonstrates the complete Machine Learning workflow—from data collection and preprocessing to model training, evaluation, and deployment—while showcasing the practical application of predictive analytics in the education and recruitment domain.

---

# 🚀 Project Objectives

The main objectives of this project are:

* 🎯 Predict the placement status of engineering students using Machine Learning techniques.
* 📊 Analyze the academic, technical, and personal factors that influence placement opportunities.
* 🧹 Perform data cleaning, preprocessing, and exploratory data analysis (EDA) to prepare high-quality data.
* ⚙️ Train and compare multiple Machine Learning classification algorithms.
* 🏆 Select the best-performing model based on evaluation metrics such as Accuracy, Precision, Recall, and F1-Score.
* 🌐 Develop an interactive Streamlit web application for real-time placement prediction.
* 📈 Provide data-driven insights that help students identify areas for improvement and enhance their employability.
* 💼 Demonstrate the practical use of Machine Learning in solving real-world education and recruitment challenges.


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

# 🛠️ Technologies Used

This project was developed using the following technologies and Python libraries:

## 💻 Programming Language

* **Python** – Core programming language used for data processing, machine learning, and application development.

## 📊 Data Analysis & Manipulation

* **Pandas** – Data loading, cleaning, transformation, and analysis.
* **NumPy** – Numerical computations and array operations.

## 📈 Data Visualization

* **Matplotlib** – Creating charts and visualizing data trends.
* **Seaborn** – Statistical data visualization and correlation analysis.

## 🤖 Machine Learning

* **Scikit-Learn** – Data preprocessing, feature engineering, model training, evaluation, and prediction.

## 💾 Model Serialization

* **Joblib** – Saving and loading the trained Machine Learning model for deployment.

## 🌐 Web Application

* **Streamlit** – Building an interactive web interface for real-time placement prediction.

## 🔧 Development Tools

* **Jupyter Notebook** – Data exploration, EDA, and model development.
* **Git & GitHub** – Version control and project hosting.


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

Exploratory Data Analysis (EDA) was performed to understand the dataset, identify meaningful patterns, detect anomalies, and discover relationships between different student attributes and placement outcomes. This step helped in selecting important features and improving the overall performance of the Machine Learning models.

## 📚 Academic Performance Analysis

The following academic factors were analyzed:

* 📈 CGPA Distribution
* 📝 10th Percentage Distribution
* 📖 12th Percentage Distribution
* 🎓 Branch-wise Student Distribution
* 📅 Attendance Percentage Analysis
* 📊 Relationship between Academic Performance and Placement

---

## 💻 Technical Skill Analysis

Technical skills play a significant role in placement opportunities. The following attributes were analyzed:

* 💡 Coding Skill Rating
* 🗣️ Communication Skill Rating
* 🧠 Aptitude Skill Rating
* 📊 Skill Score Distribution
* 📈 Skill Comparison with Placement Status

---

## 💼 Career Development Analysis

Career-related activities were analyzed to measure their impact on student placements.

* 🚀 Internships Completed
* 📂 Projects Completed
* 📜 Certifications Earned
* 🏆 Hackathon Participation
* 📊 Career Activity vs Placement Analysis

---

## 👨‍🎓 Student Demographic Analysis

Demographic information was explored to understand student diversity.

* 👥 Gender Distribution
* 🏫 Engineering Branch Distribution
* 🌆 City Tier Comparison
* 💰 Family Income Level Analysis
* 🌐 Internet Access Distribution

---

## ❤️ Lifestyle Analysis

Lifestyle factors that may influence academic performance and employability were also examined.

* 😴 Sleep Hours Distribution
* 📚 Daily Study Hours
* 😓 Stress Level Analysis
* ⚖️ Work-Life Balance
* 📈 Lifestyle Factors vs Placement

---

## 📊 Data Visualization

Several visualizations were created to better understand the dataset, including:

* Histogram
* Count Plot
* Box Plot
* Bar Chart
* Pie Chart
* Correlation Heatmap
* Pair Plot
* Distribution Plot
* Feature Correlation Matrix

The insights obtained from EDA helped identify the most influential features affecting student placement and provided a strong foundation for feature engineering, model training, and evaluation.

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

This project demonstrates how Machine Learning can help predict engineering student placement opportunities by analyzing academic, technical, and personal development factors. By comparing multiple algorithms such as Logistic Regression, Decision Tree, Random Forest, and K-Nearest Neighbors (KNN), the system identifies the most effective model and provides meaningful insights into student employability. The interactive Streamlit application enables users to explore predictions in real time, making this project a practical showcase of end-to-end Machine Learning, data preprocessing, model evaluation, and deployment skills.

---
