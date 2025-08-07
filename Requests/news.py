import requests
import json
import pyttsx3

engine = pyttsx3.init()

qur = input('What type of news: ')

api = f'https://newsapi.org/v2/everything?q={qur}&from=2025-05-06&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7'

data = requests.get(api)
# print(data.text)
news = json.loads(data.text)

for article in news['articles']:

    title = article['title']
    description = article['description']
    print(f'{title} ---> {description}')
    print('--------------------------------------------------------------------------------------')
    hii=f'title : {title} , description is :{description}'
    engine.say(hii)
    engine.runAndWait()

