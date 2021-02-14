import requests
import json

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
print("hello")
