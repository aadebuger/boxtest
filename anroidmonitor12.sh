export LEANCLOUD_API_SERVER=http://192.168.124.48:7000
cd /home/ubuntu/boxtest
sleep 30
source ~/jncloudvenv3/bin/activate
nohup python androidmonitor.py>>amonitor.out  2>&1 &
