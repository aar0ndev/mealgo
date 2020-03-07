import datetime

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
#from flask_security.utils import hash_password

from auth import hash_password, generate_alt_id
from util import to_date_int

db = SQLAlchemy()

def init_db(Meal, Plan, User):
    db.create_all()
    user = User.query.filter_by(email='user@test.com').first()
    if not user:
        user = User(
            alt_id=generate_alt_id(size=64),
            alias='dummy',
            email='user@test.com',
            password=hash_password('password'),
        )
        plan = Plan(name='dummy plan', users=[user])
        meal = Meal(
            name='dummy meal',
            created_date=datetime.datetime.utcnow(),
            planned_date=to_date_int(datetime.date.today()),
            plan=plan,
        )
        db.session.add(user)
        db.session.add(meal)
        db.session.commit()

def init_app(app):
    from models import Meal, Plan, User

    # app.config[
    #    'SQLALCHEMY_DATABASE_URI'
    # ] = 'postgres+psycopg2://postgres:postgres@db/postgres'

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    if app.config['DEBUG']:
        # Create a user to test with
        @app.before_first_request
        def create_tables_if_missing():
            # if len(sa.inspect(db.engine).get_table_names()):
                # return

            init_db(Meal, Plan, User)
            
