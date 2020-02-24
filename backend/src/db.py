import datetime

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from flask_security.utils import hash_password


db = SQLAlchemy()


def init_app(app):
    from models import Meal, Plan, Role, User

    # app.config[
    #    'SQLALCHEMY_DATABASE_URI'
    # ] = 'postgres+psycopg2://postgres:postgres@db/postgres'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    if app.config['DEBUG']:
        # Create a user to test with
        @app.before_first_request
        def create_user():
            if len(sa.inspect(db.engine).get_table_names()):
                return

            db.create_all()

            user = app.user_datastore.get_user('user@test.com')
            if not user:
                user = app.user_datastore.create_user(
                    alias='dummy',
                    email='user@test.com',
                    password=hash_password('password'),
                )
                plan = Plan(name='dummy plan', users=[user])
                meal = Meal(
                    name='dummy meal',
                    created_date=datetime.datetime.utcnow(),
                    planned_date=datetime.datetime.utcnow(),
                    plan=plan,
                )
                db.session.add(meal)
                db.session.commit()
