#server run on port 10001

from flask import Flask,request,jsonify

app = Flask(__name__)


r_ip='127.0.0.1'
r_port='10000'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/r_ip')
def set_r_ip():
    user_ip = request.remote_addr
	user_port = request.environ.get('REMOTE_PORT')
	return	jsonify(ip=user_ip,port=user_port,ip_type=type(user_ip,port_type=type(port))

    
    
