# import streamlit as st
import pickle
import numpy as np
import uvicorn
from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel
from Cardio import Cardio

app = FastAPI()

@app.get('/')
def index():
    return {"text": "Welcome to the App"}

def load_model():
    loaded_model = pickle.load(open('my_model.pkl', 'rb'))
    return loaded_model

clf = load_model()

def calc_age_bin(age):
    age_bin = 0
    if age < 30:
        age_bin = '0'
    elif age > 30 and age  < 40:
        age_bin = '1'
    elif age > 40 and age  < 50:
        age_bin = '2'
    elif age > 50 and age  < 60:
        age_bin = '3'
    elif age > 60 and age  < 70:
        age_bin = '4'
    return age_bin

def calc_bmi_class(row):
    bmi_class = 0
        
    if row < 18.5:
            bmi_class = 1
    elif row > 18.5 and row  < 24.9:
        bmi_class = 2
    elif row > 24.9 and row < 29.9:
        bmi_class = 3
    elif row > 29.9 and row < 34.9:
        bmi_class = 4
    elif row > 34.9 and row < 39.9:
        bmi_class = 5
    elif row > 39.9 and row < 49.9:
        bmi_class = 6
    return bmi_class

@app.post('/predict')
def predict_cardio(data:Cardio):
    data = data.dict()
    gender=data['gender']
    height=data['height']
    weight=data['weight']
    systolic=data['systolic']
    diastolic=data['diastolic']
    age=data['age']
    #calc age_bin
    age_bin = calc_age_bin(age)
    #calc bmi
    bmi = weight/((height/100)**2)
    #calc bmi_class
    bmi_class=calc_bmi_class(bmi)
    cholesterol=data['cholesterol']
    glucose_lvl=data['glucose_lvl']
    smoke=data['smoke']
    active=data['active']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = clf.predict([[gender, height, weight, systolic, diastolic, age, age_bin, bmi_class, cholesterol,glucose_lvl,smoke,active]])
    if(prediction[0] == 0):
        prediction="You don't Have the disease"
    else:
        prediction="You Have the disease"
    return {
        'prediction': prediction
    }
# @app.post('/predict/')
# def predict(tweet):

#     #classification
#     X = np.array([[gender, height, weight, systolic, diastolic, age, age_bin, bmi_class, cholesterol,glucose_lvl,smoke,active]])
#     X = X.astype(float)

#     dialect = clf.predict(X)
#     return {"Tweet": tweet, "Dialect":dialect[0]}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
