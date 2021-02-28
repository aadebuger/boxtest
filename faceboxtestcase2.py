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

#boxv=boxlist()
from leancloud.utils import encode
try:
    Todo = leancloud.Object.extend('Facebox')
    todo = Todo.create_without_data('60378295a43a26bd5606072d')
    todo.set('task', 6)
    todo.set('boxNumber',64)
    todo.set('imageUrl',"http://192.168.124.48:9000/boxhr/test.jpeg")
    todo.set('name',"mytest30")
    todo.save()
    print("heelo test")
except leancloud.LeanCloudError as e:
    print(e)
    if e.code == 305:
        print('操作失败！')
    else:
        raise
    