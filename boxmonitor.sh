export LEANCLOUD_API_SERVER=http://localhost:7000
cd /home/ubuntu/boxtest
sleep 30
source ~/jncloudvenv3/bin/activate
export BOX_ID=27043b125bbab5a1
export devicepass=123456
nohup python boxmonitor.py>>boxmonitor.out  2>&1 &
