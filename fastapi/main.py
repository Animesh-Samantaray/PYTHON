from fastapi import FastAPI ,  Path , HTTPException
import json
app=FastAPI()


def load_data():
    data={}
    with open('patiennts.json','r') as f:
        data=json.load(f)
    return data



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