from datetime import date


def _check_col(column):
    column_name = str(column)
    BAD_WORDS = ['pass']
    for word in BAD_WORDS:
        if word in column_name:
            return False
    return True


class SerializableModel:
    """ A general serialization scheme for SQLAlchemy models.

        For example:

            >>> from flask import Flask
            >>> from flask_sqlalchemy import SQLAlchemy
            >>> app = Flask(__name__)
            >>> app.Testing = True
            >>> app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
            >>> db = SQLAlchemy(app)
        
            >>> class User(SerializableModel, db.Model):
            ...     id = db.Column(db.Integer, primary_key=True)
            ...     first_name = db.Column(db.String(128), nullable=False)
            ...     last_name = db.Column(db.String(128), nullable=False)
            ...     email = db.Column(db.String(128), unique=True, nullable=False)
        
            >>> db.create_all()
            
            >>> u = User(id=1, first_name='Sara', last_name='Jones', email='superfan@gogo.com')
            >>> db.session.add(u)
            >>> db.session.flush()

            >>> u.to_dict()
            {'id': 1, 'first_name': 'Sara', 'last_name': 'Jones', 'email': 'superfan@gogo.com'}

            >>> repr(u)
            'User(id=1)'
    """

    def to_dict(self):
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
            if _check_col(col)
        }

    def __repr__(self):
        return (
            self.__class__.__name__
            + f'({", ".join([f"{key}={repr(getattr(self,key))}" for key in self.to_dict()])})'
        )


class ArgParser:
    """
    CLI argument parser.
    """

    def __init__(self, help=''):
        self._help = help
        self._commands = {}
        self._cmd_help = {}

    def add_command(self, cmd, func, help=''):
        self._commands[cmd] = func
        self._cmd_help[cmd] = help
        return self

    def process(self, argv):
        if len(argv) < 2:
            print('must specify command: ' + ', '.join(self._commands.keys()))
            return -1

        if argv[1] in self._commands.keys():
            self._commands[argv[1]]()
        else:
            print('unknown command: ' + argv[1])


def to_date_int(date: date):
    (date.year * 100 + date.month) * 100 + date.day


if __name__ == '__main__':
    import doctest

    doctest.testmod()
