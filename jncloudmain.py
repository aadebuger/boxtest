from flask import Flask, render_template, Response,jsonify
from flask import request
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

hostip=os.environ.get('HOSTIP',"192.168.1.8")

@app.route('/v1/route', methods=['GET','POST'])                                                                                                    
def snapshot():    
            server="wss://cn-n1-cell2.leancloud.cn/"
            server='ws://{0}:8765'.format(hostip)
            retdict={"groupId":"g0","groupUrl":"https://router-g0-push.leancloud.cn"
            ,"server":server,"ttl":10800
            ,"secondary":"wss://cn-n1-cell1.leancloud.cn/"} 
            return jsonify(retdict)
@app.route('/urlback', methods=['GET','POST'])                                                                                                    
def urlack():    
            print("request",request)

            data = request.get_data()
            print("data=",data)
            return '{“result":1,"success":true}'
if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
