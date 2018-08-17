# import gpio mode
# this mode basic can do the digital i/0
# and pwm output

# trouble with analog data...
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('import error')

#
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN)



#rasberry run on port 20002
#数据暂时还是以json 格式发送与接送

from flask import Flask
app = Flask(__name__)

server_ip='159.89.155.162'

server_port='10001'


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/channels/<int:channel>/value/<int:val>')
def set(channel,val):
    GPIO.cleanup(channel)
    GPIO.setup(channel,GPIO.OUT)
    GPIO.output(channel,val)
    return 'success'
    

if __name__=='__main__':
    app.run(debug=True)

    GPIO.cleanup()
