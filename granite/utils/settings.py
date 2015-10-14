__author__ = 'matthew'


def read_secret(path='granite/.secret/my.secret'):
    try:
        with open(path, 'r') as f:
            sk = f.read().strip()
    except IOError as e:
        raise IOError('Could not read seceret.  Please ensure %s exists and is readbale.' % path)
    if not sk:
        raise ValueError('Secrete cannot be an empty string')
    return sk
    
