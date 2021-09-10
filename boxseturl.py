import requests


#url="http://192.168.124.43:8882/sendData"
url="http://192.168.124.43:8088/sendData"

import json
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
payload={
	"serialNumber": os.environ.get("BOX_ID","3dcc6b61375ee359"),
	"devicepass": os.environ.get("devicepass","626364"),
	"tasktype": "29",
	"data": "[1,2,3]"
}

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")

