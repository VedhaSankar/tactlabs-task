from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import os

source=requests.get("https://euw.op.gg/summoner/userName=Tetetot").text
soup=BeautifulSoup(source,"lxml")
Dict=dict()
connection_string = os.getenv("connection_string")
client= MongoClient(connection_string)
d2=[]

#print(soup.prettify())

for gameitems in soup.find_all("div",class_="GameItemWrap"):
#print(gameitems.prettify())
    name =gameitems.find("div",class_="ChampionName").a.text
    k=gameitems.find("span",class_="Kill").text
    d=gameitems.find("span",class_="Death").text
    a=gameitems.find("span",class_="Assist").text
    result=gameitems.find("div",class_="GameResult").text
    lent=gameitems.find("div",class_="GameLength").text
    kda="{}/{}/{}".format(k,d,a)
    Dict["name"]=name
    Dict["kda"]=kda
    Dict["lenght"]=lent
    Dict["result"]=result.strip()
    client.Test.Test.insert_one(Dict)
    

#print(d2)
#Test.insert_many(d2)

print("Done")
