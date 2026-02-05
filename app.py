import streamlit as st
import pandas as pd
from predict import predict_loan

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="FinGuard | Loan Intelligence",
    page_icon="🏦",
    layout="wide"
)

# ================= PREMIUM BANKING CSS =================
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f1f5f9;
    }

    /* Hero Section */
    .hero-container {
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* Input Section Card */
    .input-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    /* Prediction Button */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 20px !important;
        padding: 15px !important;
        border-radius: 12px !important;
        border: none !important;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }

    /* Form Labels */
    label {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 12px !important;
        letter-spacing: 1px;
    }

    /* Input Fields */
    .stSelectbox, .stNumberInput {
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ================= HERO HEADER =================
st.markdown("""
    <div class="hero-container">
        <h1 style='color:white; margin:0;'>🏦 FinGuard AI</h1>
        <p style='color:rgba(255,255,255,0.8); font-size:18px;'>Next-Gen Loan Eligibility Assessment Tool</p>
    </div>
""", unsafe_allow_html=True)

# ================= MAIN LAYOUT =================
with st.container():
    st.markdown("### 📝 Applicant Information")
    
    # Using columns to make the form compact
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        
    with col2:
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    with col3:
        credit_history = st.selectbox("Credit History", ["1.0", "0.0"])
        loan_term = st.number_input("Loan Term (months)", min_value=0, value=360)

    st.markdown("---")
    st.markdown("### 💰 Financials")
    
    f1, f2, f3 = st.columns(3)
    with f1:
        applicant_income = st.number_input("Applicant Income ($)", min_value=0, value=5000)
    with f2:
        coapplicant_income = st.number_input("Coapplicant Income ($)", min_value=0, value=0)
    with f3:
        loan_amount = st.number_input("Loan Amount (x1000 $)", min_value=0, value=120)

# ================= PREDICTION LOGIC =================
st.write("##")

if st.button("RUN ELIGIBILITY CHECK ✨"):
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
        "Credit_History": float(credit_history)
    }

    input_df = pd.DataFrame([input_data])
    
    # Loading animation for better UX
    with st.spinner('Analyzing financial profile...'):
        prediction = predict_loan(input_df)

    st.write("---")
    
    if prediction == 1:
        st.balloons()
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.2); padding: 40px; border-radius: 20px; border: 2px solid #10b981; text-align: center;">
                <h1 style="color: #10b981; margin:0;">✅ LOAN APPROVED</h1>
                <p style="color: white; font-size: 18px;">Applicant meets all criteria for financial assistance.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background: rgba(239, 68, 68, 0.2); padding: 40px; border-radius: 20px; border: 2px solid #ef4444; text-align: center;">
                <h1 style="color: #ef4444; margin:0;">❌ LOAN REJECTED</h1>
                <p style="color: white; font-size: 18px;">Applicant does not currently meet the risk profile requirements.</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><p style='text-align: center; color: #64748b;'>FinGuard Intelligence System © 2026</p>", unsafe_allow_html=True)

