import requests
import json
import arrow
import base64
import time
from apscheduler.schedulers.background import BackgroundScheduler

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
def boxstatus():
    payload={
        "serialNumber": "068bebf627d6ab24",
        "devicepass": "123456",
        "tasktype": "23",
        "data": ""
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers).text
    print(response)

    r = json.loads(response)
    #print("taskid",r['taskid'])
    print("code",r["code"])
    for item in r["data"]:
        print(item)
    print("hello")
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
    r = json.loads(response)
    for item in r["data"]:
        print(item)
def startMonitor():
#    scheduler.add_job(event_monitor,'interval', minutes=1) 
    scheduler.add_job(boxstatus,'interval', seconds=20) 
    scheduler.add_job(personstatus,'interval', seconds=30) 
#    scheduler.add_job(appointmentUpdatetask, 'cron', hour=1, minute=10)

    scheduler.daemonic = False 
    scheduler.start()
scheduler = BackgroundScheduler()
startMonitor()
time.sleep(1000000000)
