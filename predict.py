import joblib
import pandas as pd

model = joblib.load("loan_model.pkl")

# ⚠️ EXACT order used during training
FEATURE_ORDER = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
    "Property_Area"
]

def predict_loan(input_df: pd.DataFrame):
    df = input_df.copy()

    # ---- Encoding ----
    df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})
    df["Married"] = df["Married"].map({"Yes": 1, "No": 0})
    df["Education"] = df["Education"].map({"Graduate": 1, "Not Graduate": 0})
    df["Self_Employed"] = df["Self_Employed"].map({"Yes": 1, "No": 0})
    df["Property_Area"] = df["Property_Area"].map(
        {"Urban": 2, "Semiurban": 1, "Rural": 0}
    )
    df["Dependents"] = df["Dependents"].replace("3+", 3).astype(int)

    # 🔥 FORCE same column order as training
    df = df[FEATURE_ORDER]

    prediction = model.predict(df)[0]
    return prediction


   
