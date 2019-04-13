from flask import make_response,session
from flask_login import login_required
from . import web


@web.route('/set/cookie')

def set_cookie():
    # response = make_response('hello c10')
    # response.set_cookie('name','c10',100)
    # return response
    return 'asdasd'


@web.route('/set/session')
def set_session():
    session['t'] = 1
    return 'over'



@web.route('/get/session')
def get_session():
    return str(session['t'])