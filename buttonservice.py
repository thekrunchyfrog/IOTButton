from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route('/click', methods=['POST'])
def singleClick():

    resp = Response("Message Sent", status=201, mimetype='text/plain')
    resp.headers['server'] = ""
    return resp

if __name__ == '__main__':
    app.run()
