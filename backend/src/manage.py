from app import create_app
from models import db
from util import ArgParser


def db_create_all():
    db.create_all(app=create_app())


def db_drop_all():
    db.drop_all(app=create_app())


def main(argv):
    parser = ArgParser('manage.py')
    parser.add_command('db.create_all', db_create_all)
    parser.add_command('db.drop_all', db_drop_all)
    return parser.process(argv)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
