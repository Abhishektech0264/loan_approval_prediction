import streamlit as st
from predict import predict_loan

st.set_page_config(page_title="Loan Approval App")

st.title("🏦 Loan Approval Prediction")
st.write("Enter applicant details to check loan status")

# ---- USER INPUTS ----
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0)
Loan_Amount_Term = st.number_input("Loan Term (months)", min_value=0)

Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["No", "Yes"])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# ---- MANUAL ENCODING (MATCH TRAINING) ----
Education = 1 if Education == "Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0
Property_Area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[Property_Area]

features = [
    ApplicantIncome,
    CoapplicantIncome,
    LoanAmount,
    Loan_Amount_Term,
    Credit_History,
    Education,
    Self_Employed,
    Property_Area
]

if st.button("Check Loan Status"):
    result = predict_loan(features)
    st.success(f"Loan Status: {result}")
