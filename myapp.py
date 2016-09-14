from flask import Flask, request, make_response, render_template
from hashlib import sha1


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        token = r'test'  
        signature = request.args.get('signature', '')
        echostr = request.args.get('echostr', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        tmp = [timestamp, nonce, token]
        tmp.sort()
        tmp = ''.join(tmp)
        if signature == sha1(tmp).hexdigest():
            return make_response(echostr)
        else:
            return "Access denied."


if __name__ == '__main__':
    app.run()