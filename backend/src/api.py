import datetime
import html
import json
import random

from flask import abort, render_template, request
from flask_login import login_required, current_user, login_user

import bcrypt
# from flask_security import auth_token_required, login_required
# from flask_security.core import current_user
# from flask_security.utils import login_user, verify_password

import demo
from models import Meal, Plan, User
from auth import verify_password, hash_password, get_auth_token

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

        u = User.query.filter_by(email=email).first()
        if u and u.is_active and verify_password(passwd, u.password):
            login_user(u)
            return dict(user=u.to_dict(), token=get_auth_token(u))
        return abort(401)

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

    @app.route('/api/plans', methods=['GET'])
    @login_required
    def plans():
        try:
            user = db.session.query(User).get(current_user.id)
            plans = user.plans.all()

            meals = [meal.to_dict() for plan in plans for meal in plan.meals]

            return {
                'plans': [plan.to_dict() for plan in plans],
                'meals': meals,
            }
        except Exception as e:
            return e.message

    @app.route('/api/meal', methods=['POST'])
    @login_required
    def meals():
        user = current_user
        o = request.json
        required_fields = ['name', 'planned_date', 'plan_id']
        missing_fields = [f for f in required_fields if f not in o]
        if missing_fields:
            abort(400, 'missing fields: ' + repr(missing_fields))
        # todo: check plan is owned by user
        m = Meal(name=o['name'], plan_id=o['plan_id'], planned_date=o['planned_date'],)
        db.session.add(m)
        db.session.commit()
        return m.to_dict()
        # if plan id not in plans, return error

    @app.route('/api/meal/<int:id>', methods=['DELETE'])
    @login_required
    def delete_meal(id):
        # todo: check resource owned by user
        m = db.session.query(Meal).get_or_404(id)
        db.session.delete(m)
        db.session.commit()
        return dict(status='OK')

    @app.route('/api/meal/<int:id>', methods=['GET'])
    @login_required
    def get_meal(id):
        # todo: check resource owned by user
        m = db.session.query(Meal).get_or_404(id)
        return m.to_dict()

    @app.route('/api/meal/<int:id>', methods=['PATCH'])
    @login_required
    def meal_patch(id):
        # todo: check resource owned by user
        m = db.session.query(Meal).get_or_404(id)
        patch = request.json
        if 'planned_date' in patch:
            m.planned_date = patch['planned_date']
        if 'name' in patch:
            m.name = patch['name']
        db.session.commit()
        return m.to_dict()

    @app.route('/api/demo')
    def demo_index():
        return demo.generate_data()
