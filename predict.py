import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "loan_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_loan(features):
    """
    features: list of numeric inputs in correct order
    """
    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)

    return "Approved ✅" if prediction[0] == 1 else "Rejected ❌"
