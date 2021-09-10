import requests
import json
import arrow
import base64
import leancloud
from leancloud.utils import encode
#url="http://192.168.124.43:8882/sendData"
url="http://192.168.124.43:8088/sendData"

headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }


def lessonlist():
    Student = leancloud.Object.extend('Lesson')
    query = Student.query
    query.not_equal_to("checked", 1)
    query.descending('createdAt')
    student_list = query.find()
    return student_list

import arrow
def isToday(datadate):
    today1 = arrow.utcnow()
    today=today1.to('Asia/Shanghai')
    if datadate.day==today.day and datadate.month == today.month and datadate.year == today.year:
        return True
    else:
        return False
def isTodaylesson(lesson1):
    dates = lesson1.get('dates')
    print("dates=",dates)
    if dates is None:
        return False
    for lm in dates:
        ret= isToday(arrow.get(lm))
        if ret :
            return True
    return False

def alert():
        student_list= lessonlist()
        todaylesson=filter(lambda lesson:isTodaylesson(lesson),student_list)
        todaylessonv= list(todaylesson)
        print("todaylessoonv",todaylessonv)
        for item in todaylessonv:
            value=encode(item,dump_objects=True)
            print(value)

        timev=map(lambda lesson:(lesson.get("startTime"),lesson.get("endTime")),todaylessonv)
        timelist = list(timev)
        timelist.sort(key= lambda k:k[0])
        idletime =getIdletime(timelist)
        print("idletime",idletime)
        for timeseg in idletime:
            startTime,endTime = timeseg
            uploadrule(startTime,endTime)

def removeAllrule():
	payload={
		"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
		"devicepass": os.environ.get("devicepass","626364"),
		"tasktype": "40",
		"data": ""
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print(response)

def queryrulebyid(id):
	payload={
		"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
		"devicepass": os.environ.get("devicepass","626364"),
		"tasktype": "38",
		"data": json.dumps(id)
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print(response)

def uploadrule(startTime,endTime):
		payload={
			"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
			"devicepass": os.environ.get("devicepass","626364"),
			"tasktype": "37",
			"data": {
				"name": "早上1",
				"type": 0,
				"week": "[true,true,true,true,true,true,true]",
				"startTime": startTime,
				"endTime": endTime
			}
		}

		response = requests.post(url, data=json.dumps(payload), headers=headers).text
		print(response)
		#uploadperson()
def cutlist(timev,newlist):
    for i in range(0,len(timev)-1):
            startTime,endTime=timev[i]
            startTime1,endTime1=timev[i+1]

            newlist.append((endTime,startTime1))
    return newlist

def getIdletime(timev):
    if len(timev)==0:
        return [("00:00","23:59")]
    if len(timev)==1:
        startTime,endTime=timev[0]
        return [("00:00",startTime),(endTime,"23:59")]
    if len(timev)>=2:
        count = len(timev)
        startTime,endTime=timev[0]
        startTime1,endTime1=timev[count-1]
        newlist=[]
        newlist.append(("00:00",startTime))
        cutlist(timev,newlist)
        newlist.append((endTime1,"23:59"))
        return newlist
import os
import arrow
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


os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")

def uploadboxrule():
    init_leancloud_client()
    removeAllrule()
    alert()
if __name__ == "__main__":
    # execute only if run as a script
    uploadboxrule()