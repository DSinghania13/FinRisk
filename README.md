
# 📊 FinRisk: AI at the Forefront of Financial Risk Management

**FinRisk** is a machine learning-driven credit risk prediction system designed to help lending institutions assess the likelihood of loan default using real-world financial data. The platform empowers organizations to make informed, data-backed lending decisions by leveraging advanced classification algorithms and interpretable AI models.

---

### 🖼️ User Interface Preview

The following screenshots showcase the web-based user interface used to input borrower details and view credit risk predictions in real-time.

* 📥 Input Form: Collects borrower attributes such as income, credit history, and loan amount
  
![image](https://github.com/user-attachments/assets/454de4ff-53a3-4d69-9b07-d577df2bdb53)

* 📊 Prediction Output: Displays risk classification, probability scores, and recommendations
  
![image](https://github.com/user-attachments/assets/65274480-7889-489a-af3b-64b090b7ddf2)

---

## 🧠 Project Summary

FinRisk leverages **Random Forest** and **Logistic Regression** classifiers to predict whether a loan applicant is likely to default. The system is built with a focus on:

- High **accuracy** and **recall**
- Strong **model interpretability**
- Deployment readiness via a **Flask web interface**

---

## 📁 Project Structure

```
FINRISK/
├── app/                        # Flask app code
│   ├── app.py                 # Flask backend logic
│   └── templates/
│       └── form.html          # HTML form for user input
│
├── dataset/
│   └── processed_credit_risk_dataset_encoded.csv
│
├── models/
│   ├── finRisk_model.pkl      # Trained Random Forest model
│   └── optimal_threshold.pkl  # Custom threshold object
│
├── notebooks/
│   └── FinRisk_model.ipynb    # Model training and evaluation notebook
│
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files ignored by Git
└── README.md
```

---

## 🚀 Features

- **Binary classification** of loan applicants: Default vs. No Default
- Implements **custom thresholding** for classification sensitivity
- Displays:
  - Probabilities
  - Risk categories (Low/Medium/High)
  - Model recommendation
- **Web form interface** for real-time predictions

---

## 🔍 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **ML Libraries**: scikit-learn, imbalanced-learn, pandas, numpy
- **Visualization (in notebook)**: matplotlib, seaborn

---

## 🛠️ How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/finrisk.git
cd finrisk
```

2. **Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
cd app
python app.py
```

5. **Open the browser** and visit `http://127.0.0.1:5000` to access the form.

---

## 📈 Model Details

- **Training Algorithms**:
  - Logistic Regression (baseline, interpretable)
  - Random Forest (final, high-performing)
- **Performance Metrics**:
  - **Logistic Regresion** -
    - Accuracy: 90%+
    - ROC-AUC: 0.89
  - **Random Forest** -
    - Accuracy: 90%+
    - ROC-AUC: 0.91
- **Feature Importance** used to explain predictions

---

## 📊 Dataset

The model is trained on a cleaned and encoded credit risk dataset that includes features such as:

- Age, Income
- Employment Length, Home Ownership
- Loan Purpose, Amount, Grade
- Credit History and Default Status

*(Original source: Kaggle's Lending Club dataset)*

---

## 🧪 Future Enhancements

- Integration of **XGBoost/LightGBM**
- **SHAP-based interpretability** for visual explanations
- **API endpoints** for real-time financial systems
- **Multilingual UI** for broader accessibility

---

## 👨‍💻 Authors

- [Vipransh Ojha](https://www.linkedin.com/in/vipransh-ojha/)
- Vansh Vardhan  
- [Divit Singhania](https://www.linkedin.com/in/divit-singhania-13401628a/)
- Gaurav Lodhi  
- [Abhijeet Dubey](https://www.linkedin.com/in/aiabhijeet/)

> _“Lend smarter, risk lesser” – because every informed decision counts in finance._

---
