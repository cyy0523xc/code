'''


Author: alex
Created Time: 2020年07月31日 星期五 16时25分24秒
'''
import time
from flask import Flask, render_template, request
from flask import session


app = Flask(__name__)
app.secret_key = '123abc'
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    # 设置session的有效期，即cookie的失效时间，单位是s。
    # 这个参数很重要，因为默认会话是永久性的。
    PERMANENT_SESSION_LIFETIME=3600,
)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = request.form.get('message', '')
    user = session['user'] if 'user' in session else 'None'
    print(session)
    if user != 'None':
        if session['key'] != get_key():
            session.clear()

    return render_template('index_simple.html', message=message+' '+user)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', None)
    session.clear()
    session['user'] = username
    session['time'] = time.time()
    session['key'] = get_key()
    return render_template('index_simple.html', message=username)


@app.route('/embeddable')
def embeddable():
    return "<html>I can be embedded.</html>"


def get_key():
    return request.environ['REMOTE_ADDR']+request.headers.get("User-Agent")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
