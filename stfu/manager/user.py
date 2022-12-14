from uuid import uuid4
from stfu.db import db
from stfu.manager.base import Manager
from stfu.model.user import User
from stfu.service.helper.hash import HashHelper


class UserManager(Manager):
    model_class = User

    def authenticate(self, token):
        try:
            hashed = HashHelper.get(token)
            return self.model_class.query.filter(
                self.model_class.deleted.__eq__(None),
                self.model_class.token.__eq__(hashed)
            ).first()
        except Exception as e:
            db.session.rollback()
            raise e

    def create(self, raw, user: User = None):
        raw = self.fields(raw, user)
        api_token = str(uuid4())
        token = HashHelper.get(api_token)
        raw.update({"token": token})
        try:
            # @todo ModelFactory.create here

            user = self.model_class(**raw)
            self.save(user)

            # @todo ModelEventDispatcher.dispatchCreated here

            user.api_token = api_token
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    def regenerate_token(self, id_):
        api_token = str(uuid4())
        token = HashHelper.get(api_token)
        try:
            user = self.find_or_throw(id_)
            user.token = token
            self.save(user)

            # @todo ModelEventDispatcher.dispatchUpdated here

            user.api_token = api_token
            return user
        except Exception as e:
            db.session.rollback()
            raise e
