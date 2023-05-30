#!/usr/bin/env python3
"""
Main file
"""
import typing
import bcrypt


def hash_password(password: str) -> bytes:
    '''Salt password
    '''
    pwd = password.encode()
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())
    return hashed
