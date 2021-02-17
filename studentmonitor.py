import adbutils
from leancloud.utils import encode
import requests
import base64
import time
from apscheduler.schedulers.background import BackgroundScheduler
#/Users/aadebuger/Library/Android/sdk/platform-tools
"""
{"code":0,"msg":"该箱号已经被占用5"}                                                                                             
code 0                                                                                                                   
msg 该箱号已经被占用5 
"""
url="http://192.168.124.43:8088/sendData"
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
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

def newAndroiddevice(serial):
    TestObject = leancloud.Object.extend('Androiddevice')
    test_object = TestObject()
    test_object.set('serial',serial)

    test_object.save()
    print(test_object)
def updateAndroiddevice(androido,serial):

    androido.set('serial',serial)

    androido.save()
    print(androido)
    
def studentlist():
    Todo = leancloud.Object.extend('Student')
    query = Todo.query
    query.equal_to('syncing', '1')
    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)

def studentsync(item):
        print("sync")
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        print("boxNumber",item.get("boxNumber"))
        print("name",item.get("name"))
        priint("imageUrl",item,get("imageUrl"))

    
def monitorstudent():
        slist = studentlist()
        map(lambda student:studentsync(student), list(slist))

def uploadperson(name,imageUrl,boxnumber):
    data= {
		"name": name,
		"boxnum": boxnumber,
		"type": 1,
		"takeboxPass": "123",
		"base64": ""	
        }
    ret = requests.get(imageUrl)
    print(ret)

    base64_data = base64.b64encode(ret.content)
    data['base64'] = base64_data.decode("utf8")

    payload={
		"serialNumber": "068bebf627d6ab24",
		"devicepass": "123456",
		"tasktype": "6",
		"data": json.dumps(data)
	}
    response = requests.post(url, data=json.dumps(payload), headers=headers).text
    print(response)
    retdict = json.loads(response)
    print("code",retdict['code'])
    print("msg",retdict["msg"])
    if retdict['code'] == 1:
        print("keys=",retdict["data"].keys())
        print("id=",retdict['data']["id"])        
   

def montiorlesson(lesson):
		serialv= checked(lesson)
		if len(serialv)==0:
			return 
		
def startMonitor():
#    scheduler.add_job(event_monitor,'interval', minutes=1) 
    scheduler.add_job(monitorstudent,'interval', seconds=10) 
#    scheduler.add_job(appointmentUpdatetask, 'cron', hour=1, minute=10)

    scheduler.daemonic = False 
    scheduler.start()

#kangding
import os
import json
import leancloud
from leancloud.utils import encode
#os.environ.setdefault('LEANCLOUD_API_SERVER', "http://localhost:5000")


os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")

init_leancloud_client()

scheduler = BackgroundScheduler()
startMonitor()
time.sleep(50000000) 
#uploadperson("test22","http://192.168.124.48:9000/boxhr/test.jpeg",13)