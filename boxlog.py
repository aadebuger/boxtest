import adbutils
from apscheduler.schedulers.background import BackgroundScheduler
import time

import json
import sys
import requests
import arrow
import os
url="http://192.168.124.43:8088/sendData"
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
#/Users/aadebuger/Library/Android/sdk/platform-tools
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
    
def androiddevicelist():
    Todo = leancloud.Object.extend('Androiddevice')
    query = Todo.query
    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)
def monitorp(serial):
        Todo = leancloud.Object.extend('Androiddevice')
        query = Todo.query
        query.equal_to('serial', serial);
        adevice = None
        try:
            adevice = query.first()
        except Exception as e:
            print("except ",e)
        if adevice is None:
            newAndroiddevice(serial)
        else:
            updateAndroiddevice(adevice,serial)

def montiorlesson(lesson):
		serialv= checked(lesson)
		if len(serialv)==0:
			return 
		

def lessonlist():
    Student = leancloud.Object.extend('Lesson')
    query = Student.query
    query.descending('createdAt')
    student_list = query.find()
    return student_list

def boxlist():
    Todo = leancloud.Object.extend('Box')
    query = Todo.query
    query.equal_to("action","open")

    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)

def boxmonitor():
     boxv = boxlist()
     retv=map(lambda item:boxopen(item),boxv)
     print("boxmonitor ",list(retv))
def boxopen(item):
    openbox(item.get('boxNumber'))
    item.set("action","openok")
    item.save()


def boxlog(name):
    url="http://192.168.124.43:8088/sendData"
    value=[name]
    payload={
        "serialNumber": os.environ.get("BOX_ID","270443b125bbab521"),
        "devicepass": "123456",
        "tasktype": "16",
        "data": json.dumps(value)
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).text
#    print(response)
    print("hello")
    logv = json.loads(response)
    print(logv['code'])
#    print(logv['data'])
    logdatav = logv['data']
    retv=[]
    for logitem in logdatav:
#        print(logitem)
        print(logitem['result'])
        print(logitem['time'])
        logtime= arrow.get(logitem['time'])
        print(logtime)
        print(logtime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z")
        retv.append({"boxresult":logitem['result'],"createdAt":logtime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z"})
    return retv

def boxlogbypage(first,end,firstt,endt,flag):
    url="http://192.168.124.43:8088/sendData"
    value=[first,end,firstt,endt,flag]
    payload={
        "serialNumber": os.environ.get("BOX_ID","270443b125bbab521"),
        "devicepass": "123456",
        "tasktype": "15",
        "data": json.dumps(value)
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).text
#    print(response)
    print("hello")
    logv = json.loads(response)
    print(logv['code'])
#    print(logv['data'])
    logdatav = logv['data']
    retv=[]
    for logitem in logdatav:
#        print(logitem)

#        print(logitem['result'])
#        print(logitem['time'])
#        print(logitem['name'])
        logtime= arrow.get(logitem['time'])
#        print(logtime)
#        print(logtime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z")
        retv.append({"type":logitem['type'],"name":logitem['name'],"boxresult":logitem['result'],"boxtime":logitem['time'],"createdAt1":logtime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z"})
    return retv

def boxlogbypageold(first,end,firstt,endt,flag):
    url="http://192.168.124.43:8088/sendData"
    value=[first,end,firstt,endt,flag]
    payload={
        "serialNumber": os.environ.get("BOX_ID","270443b125bbab521"),
        "devicepass":  os.environ.get("devicepass","123456"),
        "tasktype": "15",
        "data": json.dumps(value)
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).text
#    print(response)
    print("hello")
    logv = json.loads(response)
    print(logv['code'])
#    print(logv['data'])
    logdatav = logv['data']
    retv=[]
    for logitem in logdatav:
#        print(logitem)

        print(logitem['result'])
        print(logitem['time'])
        print(logitem['name'])
        logtime= arrow.get(logitem['time'])
        print(logtime)
        print(logtime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z")
        retv.append({"name":logitem['name'],"boxresult":logitem['result'],"createdAt":logtime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z"})
    return retv


import arrow
def isToday(datadate):
    today1 = arrow.utcnow()
    today=today1.to('Asia/Shanghai')
    if datadate.day==today.day and datadate.month == today.month and datadate.year == today.year:
        return True
    else:
        return False
def isWorktime(todaydate,starttime,endtime):
    todaydate=todaydate.to('Asia/Shanghai')
    nowstr = todaydate.format("HH:mm")

    print("nowstr",nowstr)
    if nowstr <starttime:
        return False
    if nowstr > endtime:
        return False
    return True
def isTodaylesson(lesson1):
    lm = arrow.get(lesson1.get('lm'))
    print("lm=",lm)
    ret= isToday(lm)
    return ret
def isLessonworktime(lesson1):
    starttime= lesson1.get('startTime')
    if starttime is None:
        return False
    endtime = lesson1.get('endTime')
    if endtime is None:
        return False
    ret =isWorktime(array.utcnow(),starttime,endtime)
    return ret

def faceboxlist():
    Todo = leancloud.Object.extend('Facebox')
    query = Todo.query
    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)

def faceboxlistbyname():
    Todo = leancloud.Object.extend('Facebox')
    query = Todo.query
    query.equal_to('name', "蔡1");
    
    query_result = query.find()

    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)

def faceboxlistbynamepage():
    Todo = leancloud.Object.extend('Facebox')
    query = Todo.query
    query.equal_to('name', "蔡");
    query.skip(1)
    query.limit(2) 

    query_result = query.find()

    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)


def faceboxlistbynamepagecount():
    Todo = leancloud.Object.extend('Facebox')
    query = Todo.query
    query.equal_to('name', "蔡");
    count = query.count()
    print("count",count)

def faceboxallpage():
    Todo = leancloud.Object.extend('Faceall')
    query = Todo.query
    query.equal_to("first", 0);
    query.equal_to("end", 10);
    query.equal_to("firstt",1577808000000)
    query.equal_to("endt",1640707200000)
    query.equal_to("flag",-1)
    query.skip(1)
    query.limit(2)    
    query_result = query.find()

    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)

def faceboxallpagecount():
    Todo = leancloud.Object.extend('Faceall')
    query = Todo.query
    query.equal_to("first", 0);
    query.equal_to("end", 10);
    query.equal_to("firstt",1577808000000)
    query.equal_to("endt",1640707200000)
    query.equal_to("flag",-1)
    query.skip(1)
    query.limit(2)    
    count = query.count()
    print("count=",count)

#kangding
import os
import json
import leancloud
from leancloud.utils import encode
#os.environ.setdefault('LEANCLOUD_API_SERVER', "http://localhost:5000")

def startMonitor():
#    scheduler.add_job(event_monitor,'interval', minutes=1) 
    scheduler.add_job(sync,'interval', minutes=1) 
#    scheduler.add_job(appointmentUpdatetask, 'cron', hour=1, minute=10)

    scheduler.daemonic = False 
    scheduler.start()

def boxlogall(timeseg):
    btime,endtime=timeseg
    bContinue=True
    begini =0 
    
    endi = begini + 20
    while bContinue:
        
        retv=boxlogbypage(begini,endi,btime,endtime,-1)
        print("len retv",len(retv))
        for item in retv:
            newFaceboxcache(item['name'],item['boxresult'],item['boxtime'],item['type'])
        print(retv)
        if len(retv)<20:
            bContinue=False
        begini = begini +20
        endi = endi + 20 

def newFaceboxcache(name,boxresult,boxtime ,type1):

    TestObject = leancloud.Object.extend('Faceboxcache')
    test_object = TestObject()


    test_object.set('name',name)  
    test_object.set('boxresult',boxresult)  
    test_object.set('boxtime',boxtime)  
    test_object.set('type',type1)  
    test_object.save()
    print(test_object)


def faceboxcachelist():
    Todo = leancloud.Object.extend('Faceboxcache')
    query = Todo.query
    query.descending('boxtime')
#mytest
#    query.ascending('boxtime')

    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)
def faceboxcachedestroy():
    Todo = leancloud.Object.extend('Faceboxcache')
    query = Todo.query
    query.descending('boxtime')
#mytest
#    query.ascending('boxtime')

    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        item.destroy()

def faceboxcachelatest():
    Todo = leancloud.Object.extend('Faceboxcache')
    query = Todo.query
    query.descending('boxtime')
#mytest
#    query.ascending('boxtime'

    try:
        query_result = query.first()
    except Exception as e:
            print("except ",e)
            return None
    return query_result.get("boxtime")

def sync():
    begini=1577808000000
    newi=faceboxcachelatest()
    if newi is not None:
        begini = newi 
    endi= int(arrow.utcnow().float_timestamp*1000)
    timeseg=begini,endi
    print("timeseg",timeseg)
    boxlogall(timeseg)

os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")

init_leancloud_client()
scheduler = BackgroundScheduler()
#boxlog()

startMonitor()

time.sleep(5000000000) 
#faceboxlist()
#faceboxlistbyname()

#time1= arrow.get()
#boxlogbypage(0,10,1577808000000,1640707200000,-1)


#faceboxallpage()
#faceboxallpagecount()
#print("next")
#faceboxlistbynamepage()
#faceboxlistbynamepagecount()



