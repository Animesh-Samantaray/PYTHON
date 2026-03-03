
from fastapi import FastAPI ,  Path , HTTPException  
from pydantic import BaseModel  , Field , computed_field 
from typing import Annotated   , Literal , Optional
import json
from fastapi.responses import JSONResponse
app=FastAPI()


class Patient(BaseModel) :
    id:Annotated[str , Field(... , description="Id of patient" , examples=['P001'])]
    name:Annotated[str , Field(... , description="Name of patient")]
    city:Annotated[str , Field(... , description="City of patient")]
    age:Annotated[int , Field(... , description="Age of patient" , lt=150 , gt=0)]
    gender:Annotated[Literal['male'  , 'female' , 'others'] , Field(... , description='Gender of patient')]
    height:Annotated[float , Field(... ,gt=0, description="height of patient in mtrs" )]
    weight:Annotated[float , Field(... ,gt=0, description="weight of patient in kgs" )]


    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel) :
    name:Annotated[Optional[str ],Field(default=None)]
    city:Annotated[Optional[str ],Field(default=None)]
    age:Annotated[Optional[int] , Field(default=None, gt=0)]
    gender:Annotated[Optional[Literal['male'  , 'female' , 'others']] , Field(default=None)]
    height:Annotated[Optional[float ], Field(gt=0, default=None )]
    weight:Annotated[Optional[float] , Field(gt=0, default=None )]

def load_data():
    try:
        with open('patients.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_data(data):
    
    with open('patients.json','w') as f:
        data=json.dump(data , f)
    return "Data saved "

@app.get('/')
def hello():
    return {
        "Message":"Patient management website "
    }


@app.get('/about')
def about():
    return {
        "Message":"Here all patient data is  availabl ein json format"
    }


@app.get('/view')
def view():
    data=load_data()
    return {
        "Message":"Data is being viewed",
        "Data":data
    }

@app.get('/view/{id}')
def view(id:str = Path(...,description='Enter id of the user ' , examples="P001")):
    data=load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404 , detail='Patient Not Found')

@app.post('/create')
def create_patient(patient:Patient):
    data=load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="User already exists")
    
    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201 , content={
        "Message":"Patient Created"
    })
    
@app.put('/edit/{patient_id}')
def update_patient(patient_id:str , patient_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient does not exist")

    existing_info=data[patient_id]
    updated_patient=patient_update.model_dump(exclude_unset=True)

    for key , value in updated_patient.items():
        existing_info[key]=value

    existing_info['id']=patient_id
    pydantic_updated_data = Patient( **existing_info)
    existing_info=pydantic_updated_data.model_dump(exclude='id')

    data[patient_id] = existing_info
    save_data(data)
    return {
        "message": "Patient updated successfully",
        "data": data[patient_id]
    }
    

    
@app.delete('/delete/{patient_id}')
def delete_data(patient_id:str):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient does not exist")
    del data[patient_id]

    save_data(data)
    return  JSONResponse(
        status_code=200,
        content= {"Message":"Patient Deleted successfully"},
    )

