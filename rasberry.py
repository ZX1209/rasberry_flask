#rasberry run on port 20002
#数据暂时还是以json 格式发送与接送

from flask import Flask
app = Flask(__name__)

server_ip='159.89.155.162'

server_port='10001'


@app.route('/')
def hello_world():
    return 'Hello, World!'
