import os

from flask import Flask

# from flask_sockets import Sockets

import api
import db
import auth

def create_app():
    global run_once
    app = Flask(__name__)

    # app.sockets = Sockets(app)
    #app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'super-secret'
    db.init_app(app)
    auth.init_app(app)
    api.init_app(app, db.db)

    @app.after_request
    def clear_server_header(response):
        response.headers['Server'] = ''
        # del response.headers['Set-Cookie']
        # response.set_cookie('session', '', expires=0, httponly=True)
        return response

    if os.environ.get('FLASK_PROFILE', '') == '1':
        from werkzeug.middleware.profiler import ProfilerMiddleware

        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[10])

    return app


app = create_app()


# add debugging for waitress
try:
    import waitress
except:
    pass
else:
    import logging

    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)

if __name__ == '__main__':

    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler

    # server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    # print('serving4eva')
    # server.serve_forever()

    app.run(debug=True)
