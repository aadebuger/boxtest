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

client1 = MongoClient(getMydbip())
def getMclient():
         return client1
client = pymongo.MongoClient(getMydbip())
change_stream = client.test_database.Lesson.watch()
for change in change_stream:
    print(dumps(change))
    print('') # for readability only
#test_database