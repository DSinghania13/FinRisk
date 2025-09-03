
# 📊 FinRisk: AI at the Forefront of Financial Risk Management

**FinRisk** is a machine learning-driven credit risk prediction system designed to help lending institutions assess the likelihood of loan default using real-world financial data. The platform empowers organizations to make informed, data-backed lending decisions by leveraging advanced classification algorithms and interpretable AI models.

## 🔗 Live Demo

Access the live project here: [View Deployed App](https://finrisk-ai.vercel.app/)

---

### 🖼️ User Interface Preview

The following screenshots showcase the web-based user interface used to input borrower details and view credit risk predictions in real-time.

* 📥 Input Form: Collects borrower attributes such as income, credit history, and loan amount
  
<img width="805" alt="Credit Risk Prediction Form" src="https://github.com/user-attachments/assets/774a4f0f-4efa-4cf3-b1b9-d160385b1673" />


* 📊 Prediction Output: Displays risk classification, probability scores, and recommendations
  
<img width="777" alt="Prediction Result" src="https://github.com/user-attachments/assets/3f9cb68a-cf17-4294-ae81-722620806001" />

---

## 🧠 Project Summary

FinRisk leverages **Random Forest** and **Logistic Regression** classifiers to predict whether a loan applicant is likely to default. The system is built with a focus on:

- High **accuracy** and **recall**
- Strong **model interpretability**
- Deployment readiness via a **Flask web interface**

---

## 📊 Visual Representation of Datasets

These Power BI dashboards provide a comprehensive **visual analysis** of credit risk-related data. They illustrate patterns in loan distribution, borrower demographics, credit history, employment length, and more — enabling data-driven insights through intuitive **visual representations**.

### Credit Risk Analysis Dashboard
This dashboard highlights the distribution of loan purposes, loan grades, home ownership, income levels, and credit history across borrowers.

![Credit Risk Analysis](https://github.com/user-attachments/assets/3566aabf-ac60-4406-abe5-d7f21db7eb6c)


### Loans Availed in 2007
This dashboard focuses on loan data from 2007, showcasing relationships between interest rates, annual income, employment length, and credit history by age.

![Loans Availed in 2007](https://github.com/user-attachments/assets/8724783b-50ba-4108-beaa-ec9ba032078b)

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

## 📊 Dataset

The model is trained on a cleaned and encoded credit risk dataset that includes features such as:

- Age, Income
- Employment Length, Home Ownership
- Loan Purpose, Amount, Grade
- Credit History and Default Status

*(Original source: Kaggle's Lending Club dataset)*

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
- [Ansh Ahuja](https://www.github.com/ansh-p1)

> _“Lend smarter, risk lesser” – because every informed decision counts in finance._

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with proper attribution.

---
.
