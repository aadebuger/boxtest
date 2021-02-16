import os
import leancloud
os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")

init_leancloud_client()

def boxlist():
    Todo = leancloud.Object.extend('Box')
    query = Todo.query


    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)

boxv=boxlist()
from leancloud.utils import encode
testbox = boxv[1]
value=encode(testbox,dump_objects=True)
print(value)
print(testbox)
testbox.set("action","open")
testbox.save()

    
    
