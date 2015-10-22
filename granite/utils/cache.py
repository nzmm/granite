__author__ = 'Matthew'

import os.path
import hashlib
from granite.settings import G_FILE_ROOT


def hashed_filename(instance, filename):
    filename = filename.lower().replace(' ', '_')
    fuzz = hashlib.md5(str(instance.site.pk).encode('utf-8') + str(instance.pk).encode('utf-8')).hexdigest()
    return "%s_%s" % (fuzz, filename)


def path_and_rename(instance, filename):
    return os.path.join(G_FILE_ROOT, hashed_filename(instance, filename))


class FSDuplicate(object):
    handle = None
    site = None

    @property
    def data(self):
        raise NotImplementedError('Any class inheriting FSDuplicate should implement their own data property')

    @property
    def fs_root(self):
        raise NotImplementedError('Any class inheriting FSDuplicate should implement their own fs_root property')

    @property
    def fs_name(self):
        return hashed_filename(self, self.handle)

    @property
    def fs_full_path(self):
        return '/'.join((self.fs_root, self.fs_name))

    def fs_dump(self):
        if not os.path.exists(self.fs_root):
            os.makedirs(self.fs_root)
        with open(self.fs_full_path, 'w') as f:
            f.write(self.data.strip())
        return
