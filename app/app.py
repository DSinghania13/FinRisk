from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the model and threshold
model = joblib.load("models/finRisk_model.pkl")
threshold = joblib.load("models/optimal_threshold.pkl")

# Define a preprocessing function
def preprocess(data):
    df = pd.DataFrame([data])
    df['person_home_ownership'] = df['person_home_ownership'].map({'MORTGAGE': 0, 'OTHER': 1, 'OWN': 2, 'RENT': 3})
    df['loan_intent'] = df['loan_intent'].map({'DEBTCONSOLIDATION': 0, 'EDUCATION': 1, 'HOMEIMPROVEMENT': 2, 'MEDICAL': 3, 'PERSONAL': 4, 'VENTURE': 5})
    df['loan_grade'] = df['loan_grade'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6})
    return df

@app.route('/')
def form():
    return render_template('form.html')  # Renders the form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()

        # Debug: Print the received input data
        print(f"Received input data: {input_data}")

        if isinstance(input_data, list):
            input_data = input_data[0]

        if not isinstance(input_data, dict):
            return jsonify({"error": "Invalid input format. Expected a flat JSON object."}), 400

        # Ensure all required features are present
        features = [
            'person_age', 'person_income', 'person_home_ownership', 'person_emp_length',
            'loan_intent', 'loan_grade', 'loan_amnt', 'loan_int_rate',
            'loan_percent_income', 'cb_person_default_on_file',
            'cb_person_cred_hist_length', 'credit_history_to_employment_ratio'
        ]

        # Create dataframe from the input data
        input_df = pd.DataFrame([{key: input_data.get(key, None) for key in features}])

        # Debug: Check for missing values in the input data
        if input_df.isnull().any().any():
            return jsonify({"error": "Input contains missing or invalid values."}), 400

        input_df['person_home_ownership'] = input_df['person_home_ownership'].map({'MORTGAGE': 0, 'OTHER': 1, 'OWN': 2, 'RENT': 3})
        input_df['loan_intent'] = input_df['loan_intent'].map({'DEBTCONSOLIDATION': 0, 'EDUCATION': 1, 'HOMEIMPROVEMENT': 2, 'MEDICAL': 3, 'PERSONAL': 4, 'VENTURE': 5})
        input_df['loan_grade'] = input_df['loan_grade'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6})

        # Debug: Print the processed input data
        print(f"Processed input data: {input_df}")

        probabilities = model.predict_proba(input_df)[:, 1]
        predictions = (probabilities >= threshold).astype(int)

        probabilities_rounded = [round(p * 100, 1) for p in probabilities]
        probabilities_rounded_neg = [round((1 - p) * 100, 1) for p in probabilities]

        prediction_messages = [
            "The person is likely to default on the loan." if pred == 1 else "The person is unlikely to default on the loan."
            for pred in predictions
        ]

        risks = []
        for prob in probabilities:
            if prob < 0.3:
                risk_label = "Low Risk"
                recommendation = "Approve with standard terms"
            elif prob < 0.7:
                risk_label = "Medium Risk"
                recommendation = "Consider additional verification or collateral"
            else:
                risk_label = "High Risk"
                recommendation = "Decline or require strong collateral"

            risks.append({
                "risk_label": risk_label,
                "recommendation": recommendation
            })

        return jsonify({
            "probabilities": {
                "P(No Default) (%)": [f"{p}%" for p in probabilities_rounded_neg],
                "P(Default) (%)": [f"{p}%" for p in probabilities_rounded]
            },
            "predictions": prediction_messages,
            "risk": risks
        })

    except KeyError as e:
        return jsonify({"error": f"Missing or incorrect feature: {e}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Data formatting issue: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=8080)
