from pymongo import MongoClient
import os

connection_string = os.getenv("connection_string")
client= MongoClient(connection_string)


post2={"hello":"123","hola":"456","adios":"789"}
client.Test.Test.insert_one(post2)
