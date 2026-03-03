from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address : Address


address_dict = {
    "city":"Bhubaneswar",
    "state":"Odisha",
    "pin":"752020"
}

address1 = Address(**address_dict)

data_dict = {
    "gender":"male",
    "name": "Animesh",
    "age": 190,
   "address":address1,
} 

patient = Patient(**data_dict)


print(patient)