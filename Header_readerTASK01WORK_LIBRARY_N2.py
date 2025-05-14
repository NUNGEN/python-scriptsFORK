from bs4 import BeautifulSoup
import requests
import pandas

url = input('Enter an URL (starts from `http://`): ')
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

for i in soup.find_all("h2"):
    print(i.response)
        
