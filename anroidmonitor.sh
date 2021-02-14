export LEANCLOUD_API_SERVER=http://192.168.1.17:7000
cd /home/ubuntu/boxtest
sleep 30
source ~/jncloudvenv3/bin/activate
nohup python androidmonitor.py &
