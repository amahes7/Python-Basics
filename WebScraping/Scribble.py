import requests
from bs4 import BeautifulSoup

r= requests.get("https://pythonhow.com/example.html")
content=r.content

soup=BeautifulSoup(content,"html.parser")

a=soup.find_all("div",{"class":"cities"})
#cities=a.find_all("h2")[0]
for item in a:
    print(item.find_all("p")[0].text)
#print(cities.text)