<<<<<<< HEAD
# loan_approval_prediction

# Loan Approval Prediction System

An end-to-end Machine Learning project that predicts whether a loan application will be **Approved** or **Rejected** based on applicant details. The project includes data preprocessing, model training, and an interactive **Streamlit web app** for real-time predictions.

---

## 🚀 Project Overview

Banks and financial institutions receive thousands of loan applications daily. Manually evaluating them is time-consuming and error-prone. This project automates loan approval decisions using a trained ML classification model.

The system takes applicant information such as income, credit history, loan amount, education, and property area, then predicts the loan status.

---
# Link to check the project 
https://loanapprovalprediction-e8nwyenr96t34hosm77ruz.streamlit.app/

## 🧠 Machine Learning Pipeline

* Data Cleaning & Preprocessing
* Handling Categorical Variables (Encoding)
* Feature Selection
* Model Training (Scikit-learn)
* Model Serialization using `joblib`
* Prediction using a trained model
* Streamlit-based UI for user interaction

---

## 📂 Project Structure

```
loan-approval-prediction/
│
├── app.py                # Streamlit web app
├── predict.py            # Model loading & prediction logic
├── train.py              # Model training script
├── loan_model.pkl        # Trained ML model
├── loan_data.csv         # Dataset
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, scikit-learn, joblib
* **Web App:** Streamlit
* **IDE:** VS Code

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd loan-approval-prediction
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model (optional)

```bash
python train.py
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧪 Sample Test Inputs

### ✅ Loan Approved Example

```
ApplicantIncome: 5500
CoapplicantIncome: 1500
LoanAmount: 120
Loan_Amount_Term: 360
Credit_History: 1
Education: Graduate
Self_Employed: No
Property_Area: Urban
```

### ❌ Loan Rejected Example

```
ApplicantIncome: 1800
CoapplicantIncome: 0
LoanAmount: 200
Loan_Amount_Term: 180
Credit_History: 0
Education: Not Graduate
Self_Employed: Yes
Property_Area: Rural
```

---

## 📈 Output

The model predicts:

* **Loan Approved** ✅
* **Loan Rejected** ❌

Results are displayed instantly in the Streamlit UI.

---

## 📌 Use Cases

* Banking & Finance loan screening
* Credit risk analysis
* FinTech applications
* ML deployment demos

---

## 🔮 Future Improvements

* Model performance optimization
* Add probability/confidence score
* Deploy on cloud (Render / Railway)
* Convert to REST API using FastAPI

---

## 👤 Author

**Abhishek Bhosale**
Machine Learning Enthusiast | Aspiring ML Engineer

---

⭐ If you like this project, feel free to star the repository!
=======
# loan_approval_prediction
>>>>>>> a977415187e6c61ea269a63c9bcb714864629694
