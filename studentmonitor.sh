export LEANCLOUD_API_SERVER=http://localhost:7000
cd /home/ubuntu/boxtest
sleep 30
source ~/jncloudvenv3/bin/activate
export BOX_ID=3dcc6b61375ee359
export devicepass=626364
nohup python studentmonitor.py>>studentmonitor.out  2>&1 &
