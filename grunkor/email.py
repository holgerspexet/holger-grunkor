import flask
from grunkor import app
from grunkor import insidan
from grunkor import PREFIX

@app.route(PREFIX + "/emails")
def emails():
    r = insidan('/users?&pageSize=1000')
    if not r.status_code == requests.codes.ok:
        1/0 # https://www.youtube.com/watch?v=dQw4w9WgXcQ

    res = [ x['login'] for x in
            r.json()['_embedded']['elements'] ]
    res = [ x for x in res if '@' in x ]
    res.sort()

    return flask.Response("\n".join(res), mimetype='text/plain')

