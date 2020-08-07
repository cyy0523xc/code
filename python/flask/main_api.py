'''


Author: alex
Created Time: 2020年07月31日 星期五 16时25分24秒
'''
import time
from flask import Flask, request
from flask import session, make_response
from flask import jsonify
from flask_cors import CORS
# from flask_session import Session


app = Flask(__name__)
app.secret_key = '123abc'
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE='Lax',
    # SESSION_COOKIE_SECURE=True,
    # SESSION_COOKIE_SAMESITE=None,
    # 设置session的有效期，即cookie的失效时间，单位是s。
    # 这个参数很重要，因为默认会话是永久性的。
    PERMANENT_SESSION_LIFETIME=360,
    SESSION_COOKIE_DOMAIN='.api.eyedmp.com',
)
resources = {"/hello": {"origins": "*"}}
resources = ['*']
CORS(app, supports_credentials=True, resources=resources)
# CORS(app, supports_credentials=True)
# CORS(app)


@app.after_request
def after_request(resp):
    resp = make_response(resp)
    # resp.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8080'
    # resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    # resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # resp.headers['Access-Control-Allow-Headers'] = 'content-type,token'
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.set_cookie('test', 'test', domain='.api.eyedmp.com',
                    secure=True, samesite=None)
    return resp


@app.route('/', methods=['GET', 'POST'])
def index():
    user = session['user'] if 'user' in session else 'None'
    print(session)
    if user != 'None':
        if session['key'] != get_key():
            session.clear()

    return jsonify(dict(session))


@app.route('/hello', methods=['POST'])
def hello():
    print(session)
    if 'user' in session:
        return jsonify({})
    return jsonify(session)


@app.route('/login', methods=['POST'])
def login():
    # username = request.form.get('username', None)
    username = 'Alex'
    set_session(username)
    return jsonify(session)


def get_key():
    return request.environ['REMOTE_ADDR']+request.headers.get("User-Agent")


def set_session(username):
    session.clear()
    session['user'] = username
    session['time'] = time.time()
    session['key'] = get_key()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)
