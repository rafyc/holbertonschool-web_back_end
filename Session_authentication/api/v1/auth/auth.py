#!/usr/bin/env python3
""" Main 0
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    '''Class Auth defines the following methods:
    - require_auth : return a boolean
    - authorization_header : return the header
    - current_user : return the user object
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if path require authentication
        :param path: the route check
        :param excluded_paths: list of route
        :return: True or False if the route check require authentication
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        for excluded_path in excluded_paths:
            check: List = excluded_path.split('*')
            if path.startswith(check[0]) or path + '/' == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method return the value of the header request
        :param request: the route requested
        :return: None or the header of the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        '''The current user
        '''
        return None

    def session_cookie(self, request=None):
        '''returns a cookie value from a request
        '''
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
