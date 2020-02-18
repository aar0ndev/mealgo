from flask_security import Security, SQLAlchemyUserDatastore

# from flask_security.utils import hash_password


def init_app(app):
    from models import User, Role
    from db import db

    app.config['SECURITY_PASSWORD_SALT'] = '7c49ep9h'
    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Auth-Token'

    # Setup Flask-Security
    app.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, app.user_datastore)
