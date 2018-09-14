from flask import Blueprint
homex = Blueprint("home",__name__)
authx = Blueprint("auth",__name__)

@homex.route('/',methods=('GET', 'POST'))
def home():
    return 'Hello World!'

@authx.route('/auth',methods=('GET', 'POST'))
def auth():
    return 'hello auth!'