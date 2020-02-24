import html
import json
import random

from flask import abort, render_template, request
from flask_security import auth_token_required
from flask_security.core import current_user
from flask_security.utils import login_user, verify_password

import demo
from models import Meal, Plan, User


def init_app(app, db):
    @app.route('/')
    def index():
        users = User.query.all()
        return json.dumps([repr(u) for u in users])

    @app.route('/api/login', methods=['POST'])
    def login():
        login_data = request.get_json(cache=False)
        email = login_data['email']
        passwd = login_data['password']

        u = app.user_datastore.get_user(email)
        if u and u.is_active and verify_password(passwd, u.password):
            # login_user(u)
            return dict(user=u.to_dict(), token=u.get_auth_token())
        return abort(401)

    # @auth_token_required
    @app.route('/api/user')
    def userinfo():
        info = (
            current_user.to_dict()
            if not current_user.is_anonymous
            else dict(
                anonymous=True, alias='unknown', id=None, email=None, logged_in=False
            )
        )
        return {'user': info}

    # @auth_token_required
    @app.route('/api/plan')
    def plans():
        try:
            user_id = 1
            if not current_user.is_anonymous:
                user_id = current_user.id

            user = db.session.query(User).get(user_id)
            plans = user.plans.all()

            meals = [meal.to_dict() for plan in plans for meal in plan.meals]

            return {
                'plans': [plan.to_dict() for plan in plans],
                'meals': meals,
            }
        except Exception as e:
            return {'error': str(e)}

    # @auth_token_required
    @app.route('/api/meal', methods=['POST'])
    def meals():
        try:
            user = db.session.query(User).get(user_id)
            plans = user.plans.all()

            # if plan id not in plans, return error

            meals = [meal.to_dict() for plan in plans for meal in plan.meals]

            return {
                'plans': [plan.to_dict() for plan in plans],
                'meals': meals,
            }
        except Exception as e:
            return {'error': str(e)}

    # @app.route('/usermeals/<int:id>')
    # def usermeals(id):
    #     return {'meals': meals_for_user(id)}

    @app.route('/api/demo')
    def demo_index():
        return demo.generate_data()

    # TODO: limit message sizes, ensure auth only
    # @app.sockets.route('/echo')
    # def echo_socket(ws):
    #     while not ws.closed:
    #         message = ws.receive()
    #         if not ws.closed:
    #             ws.send(message)

    @app.route('/debug')
    def debug():
        return render_template('socket_debug.html')
