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

def get_record():
    first = input("enter first name ")
    last = input("enter last name ")

   
    try:
        doc = coll.find_one({"first": first.lower(),"last": last.lower()})
        print("")
    except:
        print("error accessing ")
    if not doc: # if the doc we are loooking for is empty
        print("")
        print("error no result")

    return doc

def find_record():
    doc = get_record()
    if doc: # if there is content in doc
        print("")
        for k,v in doc.items(): # unpacking the dict using for loop and item()
            if k!= "_id": # here we are cheking to see if the key is nt = the id,which is automaticlly assignd by mongo
                print(k.capitalize() + ":" + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        for k,v in doc.items():
            if k != "_id":
               update_doc[k] = input(k.capitalize() + " [" + v + "] > ") # upadate_doc[k] provides d key for our update dict and the value
               # for that will be anything we put from our input prompt

               if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def add_record():
    first = input("enter first name ")
    last = input("enter last name ")
    nationality = input("enter nationaity ")
    gender = input("enter gender ")

    new_doc = {"first":first.lower(),"last":last.lower(),"nationality":nationality.lower(),"gender":gender}

    try:
        coll.insert_one(new_doc)
        print("")
        print("doc inserted")
    except:
        print("error inserting")


def delete_record():

    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove_one(doc)
                print("Document deleted!")
            except:
                print("Document not deleted")

        else:
           print("doc not deleted")



def main_loop():
    while True: # while true means it will run foreva 
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2" :
          find_record()
        elif option == "3" :
            edit_record()
        elif option == "4" :
            delete_record()
        elif option == "5" :
            conn.close() # it will close our connection
            break # exits frm the program
        else:
            print("invalid option")
        print("")

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()


