import os
from django.utils.crypto import get_random_string


def generate_secret_key(path, chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'):

        head, tail = os.path.split(path)

        if not os.path.exists(head):
            os.mkdir(head)

        sk = get_random_string(50, chars)
        # write secret to 'my.secret' file
        with open(path, 'w') as f:
            f.write(sk)
        return sk


def read_secret(path='.secret/my.secret'):
    if not os.path.exists(path):
        sk = generate_secret_key(path)
        print('Secret key successfully generated.')
    else:
        with open(path, 'r') as f:
            sk = f.read().strip()
    return sk
