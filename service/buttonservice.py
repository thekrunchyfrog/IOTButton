from flask import Flask
from flask import Response
import iotactions

app = Flask(__name__)


@app.route('/click', methods=['POST'])
def singleClick():
    try:
        iotactions.sendMessage()
        resp = Response("Message Sent", status=200, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp
    except Exception, e:
        resp = Response("Error " + e, status=500, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp

if __name__ == '__main__':
    app.run()
