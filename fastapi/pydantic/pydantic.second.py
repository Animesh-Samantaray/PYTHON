from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional



class Patient(BaseModel):
    email:EmailStr='animesh2@gmail.com'
    name:str
    age:int
    height:float
    married:bool=False
    allergies:List[str]
    contact:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com','bcci.com']
        data = value.split('@')[-1]
        if data not in valid_domains :  
            raise ValueError('Not valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
       v=value[0].upper()
       for i in range(1,len(value)):
           v+=value[i]
       return v
    


data_dict = {
    "email":"a@hdfc.com",
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
    print(patient.email)
    print(patient.age)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)

patient1 = Patient(**data_dict)


insert_patient_data(patient1)