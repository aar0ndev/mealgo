import base64
import os

import bcrypt
from flask import g
from flask.sessions import SecureCookieSessionInterface
from flask_login import LoginManager, user_loaded_from_header


def verify_password(raw_password: str, stored_password: bytes):
    pw = bytes(raw_password,'utf-8')
    return bcrypt.checkpw(pw, stored_password)

def hash_password(raw_password: str):
    pw = bytes(raw_password, 'utf-8')
    return bcrypt.hashpw(pw, bcrypt.gensalt())

def generate_alt_id(size: int):
    rand_bytes = os.urandom(int(size//4)*3)
    return base64.b64encode(rand_bytes).decode('utf-8')[:size]

def get_auth_token(user):
    return user.alt_id

def init_app(app):
    from models import User
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user_from_alt_id(user_id):
        return User.query.filter_by(alt_id=user_id).first()

    @login_manager.request_loader
    def load_user_from_request(request):

        alt_id = request.headers.get('Authentication-Token')
        if alt_id:
            user = load_user_from_alt_id(alt_id)
            if user:
                return user

        # if we could not load the user
        return None

    class CustomSessionInterface(SecureCookieSessionInterface):
        """Prevent creating session from API requests."""
        def save_session(self, *args, **kwargs):
            return

    app.session_interface = CustomSessionInterface()

    # @user_loaded_from_header.connect
    # def user_loaded_from_header_connect(self, user=None):
    #     g.login_via_header = True
