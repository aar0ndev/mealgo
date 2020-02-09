from flask import Flask
from .models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from . import api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_PASSWORD_SALT'] = '7c49ep9h'
    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'AUTH_TOKEN'
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'super-secret'
    db.init_app(app)
    api.init_app(app)

    # Setup Flask-Security
    app.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, app.user_datastore)

    # Create a user to test with
    @app.before_first_request
    def create_user():
        db.create_all()
        u = app.user_datastore.get_user('user@test.com')
        if not u:
            app.user_datastore.create_user(
                email='user@test.com', password=hash_password('password')
            )
            db.session.commit()

    return app


if __name__ == '__main__':
    app = create_app()

    app.run(debug=True)

