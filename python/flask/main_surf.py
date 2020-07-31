'''


Author: alex
Created Time: 2020年07月31日 星期五 16时25分24秒
'''
from flask import Flask, render_template, request
from flask_seasurf import SeaSurf


app = Flask(__name__)
app.secret_key = '123abc'
csrf = SeaSurf(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = request.form.get('message', None)
    return render_template('index_surf.html', message=message)


# Example of a route-specific talisman configuration
@app.route('/embeddable')
def embeddable():
    return "<html>I can be embedded.</html>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
