__author__ = 'matthew'

import os
from granite.utils.crypto import generate_secret_key


def read_secret(path='.secret/my.secret'):
    if not os.path.exists(path):
        sk = generate_secret_key(path)
        print('Secret key successfully generated.')
    else:
        with open(path, 'r') as f:
            sk = f.read().strip()
    return sk

