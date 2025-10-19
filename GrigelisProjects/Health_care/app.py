from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import pickle

# Pakraunam treniruotą modelį
with open("stroke_model.pkl", "rb") as f:
    pipeline = pickle.load(f)

app = FastAPI(title="Stroke Prediction API")

class StrokeInput(BaseModel):
    age: float
    avg_glucose_level: float
    bmi: float
    hypertension: int
    heart_disease: int
    gender: int
    ever_married: int
    work_type: int
    Residence_type: int
    smoking_status: int

@app.post("/predict")
def predict(data: StrokeInput):
    df = pd.DataFrame([{
        "age": data.age,
        "avg_glucose_level": data.avg_glucose_level,
        "bmi": data.bmi,
        "bmi_age": data.bmi * data.age,  # pipeline tikisi šio feature
        "gender": data.gender,
        "hypertension": data.hypertension,
        "heart_disease": data.heart_disease,
        "ever_married": data.ever_married,
        "work_type": data.work_type,
        "Residence_type": data.Residence_type,
        "smoking_status": data.smoking_status
    }])

    pred_proba = pipeline.predict_proba(df)[:, 1][0]
    threshold = 0.35
    pred_class = int(pred_proba >= threshold)

    return {
        "stroke_probability": float(pred_proba),
        "stroke_risk": pred_class
    }
