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


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''check password
    '''
    pwd = password.encode()
    if bcrypt.checkpw(pwd, hashed_password):
        return True
    else:
        return False
