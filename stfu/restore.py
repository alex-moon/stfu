from stfu import create_app
from stfu.db import db

if __name__ == '__main__':
    create_app()
    db.drop_all()
    db.create_all()
