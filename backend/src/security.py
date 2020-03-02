from flask_security import Security, SQLAlchemyUserDatastore

# from flask_security.utils import hash_password


def disable_cookies(app):
    # from: https://flask-login.readthedocs.io/en/latest/#disabling-session-cookie-for-apis
    from flask import g
    from flask.sessions import SecureCookieSessionInterface
    from flask_login import user_loaded_from_header

    class CustomSessionInterface(SecureCookieSessionInterface):
        """Prevent creating session from API requests."""

        def save_session(self, *args, **kwargs):
            if g.get('login_via_header'):
                return
            return super(CustomSessionInterface, self).save_session(*args, **kwargs)

    app.session_interface = CustomSessionInterface()

    @user_loaded_from_header.connect
    def user_loaded_from_header(self, user=None):
        g.login_via_header = True


def init_app(app):
    from models import User, Role
    from db import db

    app.config['SECURITY_PASSWORD_SALT'] = '7c49ep9h'

    app.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, app.user_datastore)
    disable_cookies(app)

