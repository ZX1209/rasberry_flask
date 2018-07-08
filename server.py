from flask import Flask,request,jsonify,render_template

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
    return jsonify(ip=user_ip,port=user_port)    


@app.route('/info')
def show_info():
    a_dict={"key1":10,"key2":20}
    return render_template('info.html',my_dict=a_dict)

if __name__=='__main__':
    app.run(debug=True)
