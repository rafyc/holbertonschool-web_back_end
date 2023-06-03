#!/usr/bin/env python3
'''Auth module
'''
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    '''returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw.
    '''
    pswd = password.encode("utf-8")
    hashed = bcrypt.hashpw(pswd, bcrypt.gensalt())
    if bcrypt.checkpw(pswd, hashed):
        return hashed
    else:
        pass


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        '''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(user.email))
        except NoResultFound:
            pswd = _hash_password(password=password)
            new_user = self._db.add_user(email, pswd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False


def _generate_uuid(self) -> str:
    '''generate uuid
    '''
    return str(uuid4())
