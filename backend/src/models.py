import datetime

from util import SerializableModel
from flask_login import UserMixin
from db import db

plans_users = db.Table(
    'plans_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('plan_id', db.Integer(), db.ForeignKey('plan.id')),
)


class User(SerializableModel, db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    alt_id = db.Column(db.String(64), unique=True, nullable=False)
    alias = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    #roles = db.relationship(
    #    'Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic')
    #)

    def get_id(self):
        return self.alt_id

class Meal(SerializableModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    planned_date = db.Column(db.Integer, nullable=True)
    created_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False
    )
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=True)


class Plan(SerializableModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    users = db.relationship(
        'User', secondary=plans_users, backref=db.backref('plans', lazy='dynamic')
    )
    meals = db.relationship('Meal', backref=db.backref('plan'))
