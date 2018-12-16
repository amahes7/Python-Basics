import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonhow.com/example.html")
c=r.content
soup =BeautifulSoup(c,"html.parser")
#print(soup.prettify())

a=soup.find_all("div",{"class":"cities"})

print(a)
