from pydantic import BaseModel

class Cardio(BaseModel):
    gender: float 
    height: float 
    weight: float 
    systolic: float
    diastolic: float
    age: float
    cholesterol: int
    glucose_lvl: int
    smoke: int
    active: int