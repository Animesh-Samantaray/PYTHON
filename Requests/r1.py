import requests
# print(api.text)
api='https://jsonplaceholder.typicode.com/posts'
# response=requests.get(api)
data=[ 
    { 'title':'Animesh getting data',
    'body':'It is body',
    'id':'#1233' },
    { 'title':'Animesh getting data',
    'body':'It is body',
    'id':'#1233' },
    { 'title':'Animesh getting data',
    'body':'It is body',
    'id':'#1233' },
]
headers={
    'Content-type':'application/json;charset=UTF-8',
}
response = requests.post(api,headers=headers , json=data)

print(response.text)