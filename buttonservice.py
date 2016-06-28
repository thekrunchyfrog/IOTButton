from flask import Flask
from flask import request
from flask import jsonify
from flask import Response

app = Flask(__name__)


@app.route('/click', methods=['POST'])
def api_ModelsFollowedOnline():

    if request.headers['Content-Type'] == 'application/json':
        username = request.json['username']
        password = request.json['password']
        resp.status_code = 201
        resp.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp


if __name__ == '__main__':
    app.run()
