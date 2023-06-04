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


def _generate_uuid() -> str:
    '''generate uuid
    '''
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        '''method. It takes an email string argument and returns the
        session ID as a string. The method should find the user corresponding
        to the email, generate a new UUID and store it in the database
        '''
        try:
            user = self._db.find_user_by(email=email)
            id = _generate_uuid()
            self._db.update_user(user.id, session_id=id)
            return id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id):
        ''' takes a single session_id string argument and returns
        the corresponding User or None.
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id):
        '''method takes a single user_id integer argument and returns None.
        '''
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        if email is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            id = _generate_uuid()
            self._db.update_user(user.id, reset_token=id)
            return id
        except Exception:
            raise ValueError
