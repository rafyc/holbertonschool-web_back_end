#!/usr/bin/env python3
""" Main 0
"""
from flask import request
from typing import List, TypeVar


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
        new_path = path.rstrip('/')
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
        if request is None or 'Authorization' in response:
            return None
        response = requests.get(request)
        headers = response.headers.get('Authorization')
        if headers is None:
            return None
        return headers


    def current_user(self, request=None) -> TypeVar('User'):
        '''The current user
        '''
        return request
