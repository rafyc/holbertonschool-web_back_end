#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class BasicAuth that inherits from Auth.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str)-> str:
        '''returns the Base64 part of the Authorization header for a
        Basic Authentication:
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        value = authorization_header[len('Basic '):]
        return value
