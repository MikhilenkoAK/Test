import json
import pymongo
import requests
import random
response = requests.get('https://cat-fact.herokuapp.com/facts/random')
if response.__str__() == "<Response [200]>":
    print('Connect_oK')
else:
    print('Connect_fail')
    exit(0)

#print(response.text)
y = json.loads(response.text)
#print('Interesting fact about cats: ' + y["text"])
print()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

#print(myclient.list_database_names())
dblist = myclient.list_database_names()
#if "mydatabase" in dblist:
  #print("The database exists.")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]


x = mycol.insert_many(mylist)
#print(x.inserted_ids)

#print(x)
yourRandomNumber= random.randint(1, 14)
x = mycol.find().limit(-1).skip(yourRandomNumber).next()
#print(x['name'])
print('Interesting fact about cats: ' + y["text"] +' '+ x['name'] +' thinks it is cool.')


  #удаление коллекции
x = mycol.delete_many({})

for x in mycol.find():
  print(x)
#x = mycol.insert_one(mylist)
#print(x.inserted_ids)
#print(x)
