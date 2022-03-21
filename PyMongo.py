from pymongo import MongoClient


# connection
conn = MongoClient("mongodb://IP") 
db = conn["DataBase_Name"]
collection = db.Collection_Name
for doc in collection.find():
	print(doc)

list_first_name = [ (Collection_Name.get('firstName') +' ' + Collection_Name.get('lastName') )for Collection_Name in collection.find()]
print('list_first_name: {}'.format(list_first_name))
