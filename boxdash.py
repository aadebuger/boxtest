import requests
import json
import arrow
import base64
import time
from apscheduler.schedulers.background import BackgroundScheduler

import arrow
import os 
from leancloud.utils import encode
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
def studentlist():
    Todo = leancloud.Object.extend('Student')
    query = Todo.query
    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
#        print(value)
        conv.append(item)
    return list(conv)

def newBox(boxdata,serialdict):

    TestObject = leancloud.Object.extend('Box')
    test_object = TestObject()
    test_object.set('boxNumber',boxdata['boxNumber'])
    namev= userarray2namearray(json.loads(boxdata['personidArray']),serialdict)

    test_object.set('personidArray',namev)
    test_object.set('saved',boxdata['saved'])     
                    
    test_object.set('state',boxdata['state'])
    test_object.set('type',boxdata['type'])  
    boxdate =arrow.get(boxdata['time'])
    boxdate1 = boxdate.to('Asia/Shanghai')
    test_object.set('boxtime',boxdate1.datetime)                
    test_object.save()
    print(test_object)
def updateBox(test_object,boxdata):

    test_object.set('boxNumber',boxdata['boxNumber'])
    test_object.set('personiidArray',json.loads(boxdata['personidArray']))
    test_object.set('saved',boxdata['saved'])     
                    
    test_object.set('state',boxdata['state'])
    test_object.set('type',boxdata['type'])  
    boxdate =arrow.get(boxdata['time'])
    boxdate1 = boxdate.to('Asia/Shanghai')
    test_object.set('boxtime',boxdate1.datetime)                
    test_object.save()
    print(test_object)

def userarray2namearray(useridv,serialdict):
        over=[]
        for userid in useridv:
            if userid in serialdict:
                over.append(serialdict[userid])
        return over
def updateBox(test_object,boxdata,serialdict):


    test_object.set('boxNumber',boxdata['boxNumber'])
    namev= userarray2namearray(json.loads(boxdata['personidArray']),serialdict)

    test_object.set('personidArray',namev)

    test_object.set('saved',boxdata['saved'])     
                    
    test_object.set('state',boxdata['state'])
    test_object.set('type',boxdata['type'])  
    boxdate =arrow.get(boxdata['time'])
    boxdate1 = boxdate.to('Asia/Shanghai')
    test_object.set('boxtime',boxdate1.datetime)                
    test_object.save()
    print(test_object)
def boxlist(boxNumber):
    Todo = leancloud.Object.extend('Box')
    query = Todo.query
    query.equal_to('boxNumber', boxNumber)

    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)

def boxmonitor(boxNumber,boxdata,serialdict):
     boxv = boxlist(boxNumber)
     if len(boxv)==0:
        newBox(boxdata,serialdict)
     else:
        updateBox(boxv[0],boxdata,serialdict)
#url="http://192.168.124.43:8882/sendData"
url="http://192.168.124.43:8088/sendData"

import json
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
payload={
	"serialNumber": "068bebf627d6ab24",
	"devicepass": "123456",
	"tasktype": "7",
	"data": "[0,10,0,0]"
}
def userid2student():
    serialdict={}
    studentv = studentlist()
    for item in studentv:
        serial = item.get("userid")
        name = item.get("name")
        if serial is not None:
            serialdict[serial]=name
    return serialdict

    print("serialdiict",serialdict)
def boxstatus():
    serialdict =userid2student()
    print("serialdict",serialdict)
    payload={
        "serialNumber": "068bebf627d6ab24",
        "devicepass": "123456",
        "tasktype": "23",
        "data": ""
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers).text
    print(response)
    with open('./boxstatus.json', 'w') as json_file:
        json_file.write(response)

    r = json.loads(response)
    #print("taskid",r['taskid'])
    print("code",r["code"])
    for item in r["data"]:
        print(item)
    print("hello")
    retv= map(lambda item:boxmonitor(item['boxNumber'],item,serialdict),r['data'])
    print(list(retv))
def personstatus():
    todaydate = arrow.utcnow()
    todaydate=todaydate.to('Asia/Shanghai')
    yest = todaydate.shift(days=-100)

    datav=[0,200,yest.timestamp*1000,todaydate.timestamp*1000]
    payload={
        "serialNumber": "068bebf627d6ab24",
        "devicepass": "123456",
        "tasktype": "7",
        "data": json.dumps(datav)
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).text
    with open('./persontatus.json', 'w') as json_file:
        json_file.write(response)

    r = json.loads(response)
    for item in r["data"]:
        print("p=",item)
def startMonitor():
#    scheduler.add_job(event_monitor,'interval', minutes=1) 
    scheduler.add_job(boxstatus,'interval', seconds=20) 
#    scheduler.add_job(personstatus,'interval', seconds=30) 
#    scheduler.add_job(appointmentUpdatetask, 'cron', hour=1, minute=10)

    scheduler.daemonic = False 
    scheduler.start()
import leancloud
from leancloud.utils import encode
#os.environ.setdefault('LEANCLOUD_API_SERVER', "http://localhost:5000")
#os.environ.setdefault('LEANCLOUD_API_SERVER', "http://192.168.31.82:7000")
#print(os.environ.get('LEANCLOUD_API_SERVER'))
os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")
init_leancloud_client()
scheduler = BackgroundScheduler()
startMonitor()
time.sleep(1000000000)
