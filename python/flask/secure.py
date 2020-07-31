'''


Author: alex
Created Time: 2020年07月31日 星期五 16时25分24秒
'''
from flask import Flask, render_template, request
from flask_seasurf import SeaSurf
from flask_talisman import Talisman


app = Flask(__name__)
app.secret_key = '123abc'
csrf = SeaSurf(app)

"""
"""
SELF = "'self'"
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': SELF,
        'img-src': '*',
        'script-src': [SELF, 'some.cdn.com'],
        'style-src': [SELF, 'another.cdn.com'],
    },
    # content_security_policy_nonce_in=['script-src'],
    content_security_policy_nonce_in=[],
    feature_policy={
        'geolocation': '\'none\'',
    }
)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = request.form.get('message', None)
    return render_template('index.html', message=message)


# Example of a route-specific talisman configuration
@app.route('/embeddable')
@talisman(
    frame_options='ALLOW-FROM',
    frame_options_allow_from='https://example.com/',
)
def embeddable():
    return "<html>I can be embedded.</html>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
