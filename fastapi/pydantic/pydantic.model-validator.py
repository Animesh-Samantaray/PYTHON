from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator
from typing import List , Dict , Optional



class Patient(BaseModel):
    email:EmailStr='animesh2@gmail.com'
    name:str
    age:int
    height:float
    married:bool=False
    allergies:List[str]
    contact:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls , model):
        if model.age>60 and 'emergency' not in model.contact:
            raise('User older than 60 must have emergency contact details')





data_dict = {
    "email":"a@hdfc.com",
    "name": "Animesh",
    "age": 190,
    "height": 175,
    "married": False,
    "allergies": ["dust", "pollen"],
    "contact": {
        "phone": "9876543210",
        "email": "ani@example.com",
        # "emergency":"1111111111"
    }
}


def insert_patient_data(patient :Patient ):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)

patient1 = Patient(**data_dict)


insert_patient_data(patient1)