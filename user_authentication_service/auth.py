#!/usr/bin/env python3
'''Auth module
'''

import bcrypt

def _hash_password(password : str) -> bytes:
    '''returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw.
    '''
    pswd = password.encode("utf-8")
    hashed = bcrypt.hashpw(pswd, bcrypt.gensalt())
    if bcrypt.checkpw(pswd, hashed):
        return hashed
    else:
        pass
