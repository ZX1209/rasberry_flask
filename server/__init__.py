# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


from . import routes

if __name__=='__main__':
    app.run(debug=True,threaded=True)
