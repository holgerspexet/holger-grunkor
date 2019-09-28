import flask
app = flask.Flask(__name__)
api_key = ''

PREFIX = "/grunkor"

import json
import requests


def insidan(path):
    cookie = flask.request.cookies['_open_project_session']
    return requests.get('https://insidan.holgerspexet.se/api/v3' + path,
                        cookies={'_open_project_session' : cookie})

def insidan_adm(path):
    return requests.get('https://insidan.holgerspexet.se/api/v3' + path,
                        auth=('apikey', api_key))

import grunkor.email

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=8081)
