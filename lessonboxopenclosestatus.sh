export LEANCLOUD_API_SERVER=http://localhost:7000
cd /home/ubuntu/boxtest
sleep 30
source ~/jncloudvenv3/bin/activate
nohup python lessonboxopenclosestatus.py>>lessonboxopenclosestatus.out  2>&1 &
