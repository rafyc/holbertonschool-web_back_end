#!/usr/bin/env python3
""" Main 0
"""
from flask import request
from typing import List, TypeVar

class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return path

    def authorization_header(self, request=None) -> str:
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        return request
