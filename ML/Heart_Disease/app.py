from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import sys
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from fastapi.middleware.cors import CORSMiddleware




class OutlierClipper(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.bounds = {}

    def fit(self, X, y=None):
        for col in X.columns:
            q1 = X[col].quantile(0.25)
            q3 = X[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            self.bounds[col] = (lower, upper)
        return self

    def transform(self, X):
        X = X.copy()
        for col in X.columns:
            lower, upper = self.bounds[col]
            X[col] = X[col].clip(lower, upper)
        return X
    
sys.modules['__main__'].OutlierClipper = OutlierClipper
# Load model
model = joblib.load("heart_model.pkl")

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HeartInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
    
    
@app.get('/')
def home():
    return {"message": "Heart Disease Prediction API 🚀"}


@app.post('/predict')
def predict(data:HeartInput):
    input_data = pd.DataFrame([{
    "age": data.age,
    "sex": data.sex,
    "cp": data.cp,
    "trestbps": data.trestbps,
    "chol": data.chol,
    "fbs": data.fbs,
    "restecg": data.restecg,
    "thalach": data.thalach,
    "exang": data.exang,
    "oldpeak": data.oldpeak,
    "slope": data.slope,
    "ca": data.ca,
    "thal": data.thal
    }])
    prediction = model.predict(input_data)[0]

    return {
        "prediction": int(prediction),
        "result": "Disease" if prediction == 1 else "No Disease"
    }