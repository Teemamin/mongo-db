import pymongo
import os
if os.path.exists("env.py"):
     import env


# python constants are written in caps
MONGODB_URI = os.environ.get("MONGO_URI") # it will use the os libry to get our mongo_url
DBS_NAME = "myTestDB" # our databae
COLLECTION_NAME = "myFirstMDB" # our collection

def mongo_connect(url): # to connect to database
    try:
        conn=pymongo.MongoClient(url)
        print("mongo is connected")
        return conn

    except pymongo.errors.ConnectionFaliure as e:
        print("couldnt connect %s") % e

conn = mongo_connect(MONGODB_URI) # we called oour func and passed our hidden mongouri to conncet to mongo
coll = conn[DBS_NAME][COLLECTION_NAME] # collection name whc is d connection obj,database n collection variables
# new_item = {"name":"susu","last":"hunt","nationality":"british","haircolour":"black"}
# coll.insert(new_item)
coll.update_many({"nationality":"american"},{"$set":{"hair_colour":"red"}})
documents = coll.find({"nationality":"american"}) # dis will return a mongodb obj also called a cursor

for doc in documents: # iterating to unpackage it
    print(doc)