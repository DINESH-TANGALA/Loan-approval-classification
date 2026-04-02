#  Loan Approval Prediction System

A Machine Learning-powered web application that predicts the likelihood of loan approval based on user demographics, financial history, and credit scores. Built with **Python**, **Scikit-Learn**, and **Streamlit**.

---

##  Project Overview
This project aims to help users understand their loan eligibility before a formal bank inquiry. The model is trained on the "USA Loan Approval" dataset and optimized to handle real-world banking constraints, such as high-impact credit defaults and CIBIL score thresholds.

### Key Features:
* **Predictive Modeling:** Uses a Random Forest Classifier with Hyperparameter Tuning.
* **Interactive UI:** A user-friendly Streamlit dashboard for real-time predictions.
* **Data Pipeline:** Handles missing value imputation, manual ordinal mapping, and One-Hot Encoding.
* **Robust Logic:** Optimized to avoid overfitting (96% Train / 92% Test accuracy).

---

##  Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy, Scikit-Learn, Pickle
* **Frontend:** Streamlit
* **Model:** RandomForestClassifier (Optimized via GridSearchCV)

---

##  Model Performance
The model was refined to ensure it doesn't just "memorize" data but learns actual banking patterns:
| Metric | Training Score | Testing Score |
| :--- | :--- | :--- |
| **Accuracy** | 96% | 92% |

> **Note:** The model specifically prioritizes "Previous Defaults" and "CIBIL Scores" to reflect realistic lending risks.

