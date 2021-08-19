import requests


#url="http://192.168.124.43:8882/sendData"
url="http://192.168.124.43:8088/sendData"

import json
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
payload={
	"serialNumber": os.environ.get("serialNumber","27043b125bbab5a1"),
	"devicepass": os.environ.get("devicepass","123456"),
	"tasktype": "29",
	"data": "[1,2,3]"
}

response = requests.post(url, data=json.dumps(payload), headers=headers).text
print(response)
print("hello")

