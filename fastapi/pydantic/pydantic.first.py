from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional



class Patient(BaseModel):
    email:EmailStr='animesh2@gmail.com'
    name:str
    age:int=Field(gt=0 , lt=150)
    height:float =Field(gt=0)
    married:bool=False
    allergies:Optional[List[str]]=None
    contact:Optional[Dict[str,str]]=None


data_dict = {
    "name": "Animesh",
    "age": 190,
    "height": 175,
    "married": False,
    "allergies": ["dust", "pollen"],
    "contact": {
        "phone": "9876543210",
        "email": "ani@example.com"
    }
}


def insert_patient_data(patient :Patient ):
    print(patient.name)
    print(patient.age)

patient1 = Patient(**data_dict)


insert_patient_data(patient1)