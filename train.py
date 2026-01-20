import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv("C:\\Users\\bhosa\\MACHINE_LEARNING\\loan-approval-prediction\\loan_data.csv")

# Drop Loan_ID if exists
if "Loan_ID" in df.columns:
    df.drop("Loan_ID", axis=1, inplace=True)

# Separate target
y = df["Loan_Status"]
X = df.drop("Loan_Status", axis=1)

# Target encode
y = y.map({"Y": 1, "N": 0})

# Column types
categorical_cols = X.select_dtypes(include="object").columns
numeric_cols = X.select_dtypes(exclude="object").columns

# Preprocessing
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_cols),
        ("cat", categorical_transformer, categorical_cols)
    ]
)

# Full pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
pipeline.fit(X_train, y_train)

# Save pipeline
joblib.dump(pipeline, "loan_pipeline.pkl")

print("✅ Pipeline trained & saved as loan_pipeline.pkl")



