import requests
from bs4 import BeautifulSoup
url='https://react.dev/learn/thinking-in-react';
data=requests.get(url)
soup=BeautifulSoup(data.text,'html.parser')
# print(soup.prettify())
for heading in soup.find_all('h1'):
    print(heading.text)