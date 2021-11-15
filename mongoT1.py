import  pymongo
from pymongo import MongoClient
import os

connection_string = os.getenv("connection_string")
client = MongoClient(connection_string)
db=client.admin

print("idk me just try")
#print(serverStatusResult=db.command("serverStatus"))

post1={"name":"vedha","score":5}
client.Test.Test.insert_one(post1)
