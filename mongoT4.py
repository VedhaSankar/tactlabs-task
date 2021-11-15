from pymongo import MongoClient
import os

connection_string = os.getenv("connection_string")
client= MongoClient(connection_string)

# Creating a database

mydb=client["mydb"]

mycol=mydb["people"]
data={"name":'john','age':30}
mycol.insert_one(data)

datalist=[{"name":'akali','age':18},{"name":'rids','age':3}]
mycol.insert_many(datalist)

# to see available databases
print(client.list_database_names())

# to see available collections
print(mydb.list_collection_names())

# finding items:
for x in mycol.find({"name":"akali"}):
    print(x)

#for x in mycol.find({"age":{"$gte:5"}}):
 #   print(x)

for x in mycol.find({"name":"akali"},{"name":1,"_id":0}):
    print(x)

# printing all docs
for x in mycol.find():
    print(x)

print("done")
