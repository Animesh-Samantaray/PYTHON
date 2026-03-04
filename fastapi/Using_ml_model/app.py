from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware
from schema.pydantic_model import UserInput
from model_.model import model
app=FastAPI()
MODEL_VERSION="1.0.0"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



    
@app.get('/')
def home():
    return {"Message":"Home Page"}

@app.get('/health')
def home():
    return {"Status":"Good","Version":MODEL_VERSION}

@app.post('/predict')
def predict_premium(data:UserInput):

    input=pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }])


    prediction=model.predict(input)[0]

    return JSONResponse(status_code=200, content={
                            'predicted':prediction
                        })
