# -*- coding: utf-8 -*-

from flask import Flask,request,jsonify,render_template

app = Flask(__name__)


r_ip='127.0.0.1'
r_port='10000'


posts=[ {'key':'温度',
         'value':12
         },
         {'key':'湿度',
         'value':12
         },
         {'key':'氧气',
         'value':12
         },
         {'key':'阳光',
         'value':12
         },
         {'key':'声音',
         'value':12
         }]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/r_ip')
def set_r_ip():
    user_ip = request.remote_addr
    user_port = request.environ.get('REMOTE_PORT')
    return jsonify(ip=user_ip,port=user_port)    


@app.route('/info',methods=['GET'])
def show_info():
    
    return render_template('info.html',posts=posts)

@app.route('/info',methods=['POST'])
def post_info():
    global posts
    json_data=request.get_json(force=True)
    print(json_data)
    print(json_data[0])
    print(type(json_data))
    print(type(json_data[0]))
    posts=json_data
    return 'ok'

if __name__=='__main__':
    app.run(debug=True)
