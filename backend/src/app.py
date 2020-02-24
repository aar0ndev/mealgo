from flask import Flask

# from flask_sockets import Sockets

import api
import db
import security


def create_app():
    app = Flask(__name__)
    # app.sockets = Sockets(app)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'super-secret'
    db.init_app(app)
    security.init_app(app)
    api.init_app(app, db.db)

    @app.after_request
    def clear_server_header(response):
        response.headers['Server'] = ''
        return response

    return app


app = create_app()

if __name__ == '__main__':

    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler

    # server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    # print('serving4eva')
    # server.serve_forever()
    app.run(debug=True)
