import os
from django.utils.crypto import get_random_string


def generate_secret_key(chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'):

        if not os.path.exists('.secret'):
            os.mkdir('.secret')

        sk = get_random_string(50, chars)
        # write secret to the my.secret file
        with open('.secret/my.secret', 'w') as f:
            f.write(sk)
        return sk
