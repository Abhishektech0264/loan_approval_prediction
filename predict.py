import joblib
import numpy as np

pipeline = joblib.load("loan_pipeline.pkl")

def predict_loan(input_df):
    prediction = pipeline.predict(input_df)
    return prediction[0]
def predict_loan(features):
    input_array = np.array(features).reshape(1, -1)
    prediction = pipeline.predict(input_array)
    return "Approved" if prediction[0] == 1 else "Rejected"     
