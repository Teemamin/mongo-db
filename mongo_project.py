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
        return conn

    except pymongo.errors.ConnectionFaliure as e:
        print("couldnt connect %s") % e


def show_menu():
    print("")
    print("1. add a record ")
    print("2. find a record by name ")
    print("3. edit a record ")
    print("4. delete a record ")
    print("5. exit ")

    option = input("enter option: ")
    return option


def main_loop():
    while True: # while true means it will run foreva 
        option = show_menu()
        if option == "1":
            print("you have selected option 1 ")
        elif option == "2" :
            print("you have selected option 2 ")
        elif option == "3" :
            print("you have selected option 3 ")
        elif option == "4" :
            print("you have selected option 4 ")
        elif option == "5" :
            conn.close() # it will close our connection
            break # exits frm the program
        else:
            print("invalid option")
        print("")

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()


