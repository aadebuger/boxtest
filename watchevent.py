import os
import pymongo
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import collection
#from pymongo import ReturnDocument

import os
from pymongo import collection
from bson import json_util
from bson.objectid import ObjectId
def getMydbip():

    return "mongodb://root:root13906917736@{0}:27017/".format(os.environ.get('MYDB_PORT_27017_TCP_ADDR',"127.0.0.1"))

print("watch event ..........\n")
client1 = MongoClient(getMydbip())
def getMclient():
         return client1
client = pymongo.MongoClient(getMydbip())
change_stream = client.test_database.event.watch()
for change in change_stream:
    print(dumps(change))
    print("change=",change["_id"])
    print('') # for readability only
    operationType=change["operationType"]
    documentKey=change["documentKey"]
    print("oiid=",documentKey["_id"])
    print("oid=",str(documentKey["_id"]))
    action = change['fullDocument']["action"]
    print("action=",action)
    print("change ovoer\n")
#test_database