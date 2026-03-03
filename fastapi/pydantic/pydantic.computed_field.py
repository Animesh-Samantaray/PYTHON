from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator,computed_field
from typing import List , Dict , Optional



class Patient(BaseModel):
    email: EmailStr = 'animesh2@gmail.com'
    name: str
    age: int
    height: float
    weight: float
    married: bool = False
    allergies: List[str]
    contact: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    


data_dict = {
    "email":"a@hdfc.com",
    "name": "Animesh",
    "age": 190,
    "height": 1.75,
    "weight":67.0,
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
    print(patient.calculate_bmi)

patient1 = Patient(**data_dict)


insert_patient_data(patient1)