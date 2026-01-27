import streamlit as st
import pandas as pd
from predict import predict_loan

st.set_page_config(page_title="Loan Approval Prediction")

st.title("🏦 Loan Approval Prediction")
st.write("Enter applicant details to check loan status")

# ---------- USER INPUTS ----------
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount x 1000", min_value=0)
loan_term = st.number_input("Loan Term (months)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])

# ---------- PREDICTION ----------
if st.button("Predict Loan Status"):
    input_data = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "Property_Area": property_area,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history
    }

    input_df = pd.DataFrame([input_data])

    prediction = predict_loan(input_df)

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")


