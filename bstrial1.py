from bs4 import BeautifulSoup
import requests

with open("ordered list.html") as html_file:
    soup= BeautifulSoup(html_file,"lxml")

#print(soup.prettify())
    
matcha= soup.title.text
print(matcha)
