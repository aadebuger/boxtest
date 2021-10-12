import requests
import json
import arrow
import base64
#url="http://192.168.124.43:8882/sendData"
url="http://192.168.124.43:8088/sendData"

import json
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
payload={
	"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
	"devicepass": os.environ.get("devicepass","626364"),
	"tasktype": "7",
	"data": "[0,10,0,0]"
}

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")
payload={
	"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
	"devicepass": os.environ.get("devicepass","626364"),
	"tasktype": "7",
	"data": "[0,100,0,0]"
}

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")

payload={
	"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
	"devicepass": os.environ.get("devicepass","626364"),
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


print("hello")
def querybyid(id):
	idv=[id]
	payload={
		"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
		"devicepass": os.environ.get("devicepass","626364"),
		"tasktype": "9",
		"data": json.dumps(idv)
	}
	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print("query by id=",response)
	print("hello")
for id in range(1,100):
	querybyid(id)

def queryrulebyid(id):
	payload={
		"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
		"devicepass": os.environ.get("devicepass","626364"),
		"tasktype": "38",
		"data": json.dumps(id)
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print(response)

def uploadperson():
	data= {
		"name": "测试2",
		"boxnum": 1,
		"type": 1,
		"takeboxPass": "123",
		"base64": ""	}
	with open("test.jpeg","rb") as f:
		base64_data = base64.b64encode(f.read())
		data['base64'] = base64_data.decode("utf8")

	payload={
		"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
		"devicepass": os.environ.get("devicepass","626364"),
		"tasktype": "6",
		"data": json.dumps(data)
	}
	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	print(response)


queryrulebyid(72)
def uploadrule():
		payload={
			"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
			"devicepass": os.environ.get("devicepass","626364"),
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

datav=[0,200,yest.timestamp*1000,todaydate.timestamp*1000]
payload={
	"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
	"devicepass": os.environ.get("devicepass","626364"),
	"tasktype": "7",
	"data": json.dumps(datav)
}
response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)	

