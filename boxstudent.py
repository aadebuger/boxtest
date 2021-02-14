import requests
import json
import arrow
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

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")
payload={
	"serialNumber": "068bebf627d6ab24",
	"devicepass": "123456",
	"tasktype": "7",
	"data": "[0,100,0,0]"
}

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")

payload={
	"serialNumber": "068bebf627d6ab24",
	"devicepass": "123456",
	"tasktype": "23",
	"data": ""
}

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)

r = json.loads(response)
print(r)
#print("taskid",r['taskid'])
print("code",r["code"])
print("data",r["data"])
for item in r["data"]:
	print(item)
print("hello")


todaydate = arrow.utcnow()
todaydate=todaydate.to('Asia/Shanghai')
yest = todaydate.shift(days=-100)

datav=[0,100,yest.timestamp*1000,todaydate.timestamp*1000]
payload={
	"serialNumber": "068bebf627d6ab24",
	"devicepass": "123456",
	"tasktype": "7",
	"data": json.dumps(datav)
}
response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")
idv=[1]
payload={
	"serialNumber": "068bebf627d6ab24",
	"devicepass": "123456",
	"tasktype": "9",
	"data": json.dumps(idv)
}
response = requests.post(url, data=json.dumps(payload), headers=headers).text
print("query by id=",response)
print("hello")