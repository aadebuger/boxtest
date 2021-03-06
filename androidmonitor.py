import adbutils

from leancloud.utils import encode
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

def newAndroiddevice(serial,name,model,device,status):
    TestObject = leancloud.Object.extend('Androiddevicenew')
    test_object = TestObject()
    test_object.set('serial',serial)
    test_object.set('name',name)
    test_object.set('model',model)
    test_object.set('device',device)
    test_object.set('status',status)
    test_object.save()
    print(test_object)
def updateAndroiddevice(androido,serial,name,model,device,status):

    androido.set('serial',serial)
    androido.set('name',name)
    androido.set('model',model)
    androido.set('device',device)
    androido.set('status',status)    
    androido.save()
    print(androido)
def updateAndroiddevicestatus(androido,status):

    androido.set('status',status)    
    androido.save()
    print(androido)
       
def androiddevicelist():
    Todo = leancloud.Object.extend('Androiddevicenew')
    query = Todo.query
    
    query_result = query.find()
    conv=[]
    for item in query_result:
        print(item)
        value=encode(item,dump_objects=True)
        print(value)
        conv.append(item)
    return list(conv)
def monitorp(serial,name,model,device,status):
		devicesvv= androiddevicelist()
		devicesv= list(devicesvv)
		if len(devicesv)==0:
			newAndroiddevice(serial,name,model,device,status)
		else:
			updateAndroiddevice(devicesv[0],serial,name,model,device,status)
def monitorpstatus(serial,status):
		devicesvv= androiddevicelist()
		devicesv= list(devicesvv)
		if len(devicesv)==0:
			pass
		else:
			updateAndroiddevicestatus(devicesv[0],status)


#kangding
import os
import json
import leancloud
from leancloud.utils import encode
#os.environ.setdefault('LEANCLOUD_API_SERVER', "http://localhost:5000")
#os.environ.setdefault('LEANCLOUD_API_SERVER', "http://192.168.31.82:7000")
#print(os.environ.get('LEANCLOUD_API_SERVER'))
os.environ['LEANCLOUD_API_SERVER'] = os.environ.get('LEANCLOUD_API_SERVER',"http://192.168.31.82:7000")
init_leancloud_client()
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())

devices=adb.track_devices()
for item in devices:
	print(item)
	print(item.serial)
	if item.status=='device':
		print("device")
		d = adb.device(serial=item.serial)
		serial = d.shell(["getprop", "ro.serial"])
		print("serial",serial)
		print(d.prop.name)
		print(d.prop.model)
		print(d.prop.device)
		print(d.prop.get("ro.product.model"))
		monitorp(item.serial,d.prop.name,d.prop.model,d.prop.device)
	else:
		monitopstatus(item.serial,item.status)
