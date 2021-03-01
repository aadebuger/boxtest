import requests
import json
import arrow
import base64
import leancloud
#url="http://192.168.124.43:8882/sendData"
url="http://192.168.124.43:8088/sendData"




def lessonlist():
    Student = leancloud.Object.extend('Lesson')
    query = Student.query
    query.not_equal_to("checked", 1)
    query.descending('createdAt')
    student_list = query.find()
    return student_list

def alert():
        student_list= lessonlist()
        todaylesson=filter(lambda lesson:isTodaylesson(lesson),student_list)
        todaylessonv= list(todaylesson)
        print("todaylessoonv",todaylessonv)

        timev=map(lambda lesson:(lesson.get("stateTime"),lesson.get("endTime"),todyalessonv))
        timelist = list(timev)
        timelist.sort(key= lambda k:k[0])
        idletime =getIdletime(timelist)
        print("idletime",idletime)

def removeAllrule():
	payload={
		"serialNumber": "068bebf627d6ab24",
		"devicepass": "123456",
		"tasktype": "40",
		"data": ""
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print(response)

def queryrulebyid(id):
	payload={
		"serialNumber": "068bebf627d6ab24",
		"devicepass": "123456",
		"tasktype": "38",
		"data": json.dumps(id)
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print(response)

def uploadrule():
		payload={
			"serialNumber": "068bebf627d6ab24",
			"devicepass": "123456",
			"tasktype": "37",
			"data": {
				"name": "早上1",
				"type": 0,
				"week": "[true,false,true,true,true,true,true]",
				"startTime": "00:00",
				"endTime": "23:59"
			}
		}

		response = requests.post(url, data=json.dumps(payload), headers=headers).text
		print(response)
		#uploadperson()
alert()
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
removeAllrule()