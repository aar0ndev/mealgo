from .models import db, User
from . import demo
import json
import html
import random
from flask_security import auth_token_required
from flask_security.utils import login_user, verify_password
from flask import abort, request


def init_app(app):
    @app.after_request
    def clear_server_header(response):
        response.headers['Server'] = ''
        return response

    @app.route('/')
    def index():
        users = User.query.all()
        return json.dumps([u.to_dict() for u in users])

    @app.route('/login', methods=['POST'])
    def login():
        login_data = request.get_json(cache=False)
        email = login_data['email']
        passwd = login_data['password']

        u = app.user_datastore.get_user(email)
        if u and u.is_active and verify_password(passwd, u.password):
            # login_user(u)
            return u.get_auth_token()
        return abort(401)

    @app.route('/userinfo')
    @auth_token_required
    def userinfo():

        return {'user': 'info here'}

    @app.route('/demo')
    def index():
        return demo.generate_data()
