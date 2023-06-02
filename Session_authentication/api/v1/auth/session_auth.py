#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth
import uuid
import os
from models.user import User


class SessionAuth(Auth):
    '''
    '''
    pass

    user_id_by_session_id = {}
    session_name = os.getenv('SESSION_NAME')

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id:
        '''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_uuid = str(uuid.uuid4())
        self.user_id_by_session_id[session_uuid] = user_id
        return session_uuid

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' that returns a User ID based on a Session ID:
        '''
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        ''' returns a User instance based on a cookie value:
        '''
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        del self.user_id_by_session_id[session_id]
        return True
