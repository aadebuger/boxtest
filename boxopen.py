url="http://192.168.124.43:8088/sendData"

import json
import sys
import requests
headers = {
    "Content-Type": "application/json; charset=UTF-8"
    }
def openbox(i):
    boxv=[i]
    payload={
        "serialNumber": "27043b125bbab5a1",
        "devicepass": "123456",
        "tasktype": "24",
        "data": json.dumps(boxv)
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).text
    print(response)
    print("hello")
if __name__ == "__main__":
    # execute only if run as a script
    openbox(sys.argv[1])

