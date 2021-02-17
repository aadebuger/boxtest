import os
import leancloud
from leancloud.utils import encode
os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")

def init_leancloud_client():
    import os

    LEANCLOUD_APP_ID = os.environ.get("LEANCLOUD_APP_ID", "rGngnUit9fqERRVjQMfzQhWg-gzGzoHsz")
    LEANCLOUD_APP_KEY = os.environ.get("LEANCLOUD_APP_KEY", "xWQ3c4CoLPXIlRd6UxLRGndX")
    LEANCLOUD_MASTER_KEY = os.environ.get("LEANCLOUD_MASTER_KEY", "x3cl6OYR2mC6dDQsW0dMeceJ")
    LEANCLOUD_REGION = os.environ.get("LEANCLOUD_REGION", "CN")
    leancloud.init(app_id=LEANCLOUD_APP_ID, app_key=LEANCLOUD_APP_KEY, master_key=LEANCLOUD_MASTER_KEY)
    leancloud.use_region(LEANCLOUD_REGION)
    print("leancloud init success with app_id: {}, app_key: {}, region: {}".format(LEANCLOUD_APP_ID, LEANCLOUD_APP_KEY,
                                                                                   LEANCLOUD_REGION))

init_leancloud_client()

def newStudent(name,androidid,boxNumber):

    TestObject = leancloud.Object.extend("Student")
    test_object = TestObject()
    test_object.set('name',name)
    test_object.set('android',androidid)
    test_object.set('boxNumber',boxNumber)
    test_object.save()
    print(test_object)
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
newStudent("test22","M22","8")