from flask_restplus import fields

from stfu.api import api
from stfu.db import db
from stfu.model.base import BaseModel


class UserTier:
    Viewer = 0
    User = 1
    God = 2


class User(db.Model, BaseModel):
    FIELDS = [
        'name',
        'email',
    ]
    GOD_FIELDS = [
        'tier',
    ]

    api_token: str = None

    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False)
    tier = db.Column(db.Integer, nullable=False, default=0)

    schema = api.model('User', {
        'id': fields.Integer,
        'email': fields.String,
        'name': fields.String,
        'api_token': fields.String,
        'created': fields.DateTime(),
        'updated': fields.DateTime(),
        'deleted': fields.DateTime(),
    })
