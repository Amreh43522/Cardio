from pydantic import BaseModel

class Cardio(BaseModel):
    gender1-fand2-m: float 
    heightincm: float 
    weightincm: float 
    systolic: float
    diastolic: float
    age: float
    cholesterol: int
    glucose_lvl: int
    smoke0-non1-smoker: int
    active: int
