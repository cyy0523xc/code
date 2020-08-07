'''


Author: alex
Created Time: 2020年07月31日 星期五 16时25分24秒
'''
import time
from flask import Flask, render_template, request
from flask import session
from flask import jsonify
from flask_cors import CORS
# from flask_session import Session


app = Flask(__name__)
app.secret_key = '123abc'
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    # 设置session的有效期，即cookie的失效时间，单位是s。
    # 这个参数很重要，因为默认会话是永久性的。
    PERMANENT_SESSION_LIFETIME=10,
)
CORS(app, supports_credentials=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = request.form.get('message', '')
    user = session['user'] if 'user' in session else 'None'
    print(session)
    if user != 'None':
        if session['key'] != get_key():
            session.clear()

    return render_template('index_simple.html', message=message+' '+user)


@app.route('/hello', methods=['POST'])
def hello():
    if 'user' not in session:
        return jsonify({})
    return jsonify(session)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', None)
    set_session(username)
    return jsonify(session)
    # return render_template('index_simple.html', message=username)


@app.route('/embeddable')
def embeddable():
    return "<html>I can be embedded.</html>"


def get_key():
    return request.environ['REMOTE_ADDR']+request.headers.get("User-Agent")


def set_session(username):
    session.clear()
    session['user'] = username
    session['time'] = time.time()
    session['key'] = get_key()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
