export LEANCLOUD_API_SERVER=http://192.168.124.48:7000
cd /home/ubuntu/boxtest
sleep 30
source ~/jncloudvenv3/bin/activate
export BOX_ID=27043b125bbab5a1
export devicepass=123456
nohup python boxdash.py>>boxdash.out  2>&1 &
