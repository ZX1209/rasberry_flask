#rasberry run on port 20002
#数据暂时还是以json 格式发送与接送
import sqlite3
import datetime
from flask import Flask,jsonify,g, request,render_template
app = Flask(__name__)

DATABASE = 'test.db'

def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database=sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database',None)
    if db is not None:
        db.close()


server_ip='159.89.155.162'

server_port='10080'

local_ip = '127.0.0.1'
local_port = '5000'

@app.route('/layui/test')
def layui_test():
    return render_template("layui-lab.html")

@app.route('/test/db')
def test_db():
    cur = get_db().cursor()
    cur.execute('select * from alldata order by time limit 10')
    tmp = cur.fetchall()
    return jsonify(result=tmp)



@app.route('/test/delta/hour/<int:deltahour>')
def get_delta_data(deltahour):
    cur = get_db().cursor()
    dis = datetime.timedelta(hours=deltahour)
    nowt = datetime.datetime.now()
    dist = nowt-dis
    t = (str(dist),)
    cur.execute("select * from alldata where time>?",t)
    tmp = cur.fetchall()
    return jsonify(result=tmp)




'''
@app.route('/channels/<int:channel>/value/<int:val>')
def set(channel,val):
    GPIO.cleanup(channel)
    GPIO.setup(channel,GPIO.OUT)
    GPIO.output(channel,val)
    return 'success'
''' 



# from server

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

# home page
@app.route('/',methods=['GET'])
def get_homepage():
    return render_template('data_page.html')

# 测试
@app.route('/hello')
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
    posts=json_data
    return 'ok'



# charts
@app.route('/charts')
def get_charts():
    return render_template('charts.html')


if __name__=="__main__":
    app.run(debug=True)
