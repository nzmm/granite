__author__ = 'Matthew'

import os


class FSDuplicate(object):
    ASSET_TYPE_NAME = ''
    TEMPLATE_REL_ROOT = ''
    FS_ROOT = ''
    # stubs
    handle = None
    site = None

    @property
    def fs_path(self):
        if self.ASSET_TYPE_NAME == 'text':
            return self.FS_ROOT
        return '/'.join((self.FS_ROOT, self.site.handle))

    @property
    def fs_name(self):
        return self.handle.lower().replace(' ', '_')

    @property
    def fs_full_path(self):
        return '/'.join((self.fs_path, self.fs_name))

    @property
    def template_path(self):
        # django relative template path
        if self.ASSET_TYPE_NAME == 'text':
            return '/'.join(p for p in (self.TEMPLATE_REL_ROOT, self.fs_name) if p.strip())
        return '/'.join(p for p in (self.TEMPLATE_REL_ROOT, self.site.handle, self.fs_name) if p.strip())

    @property
    def data(self):
        raise NotImplementedError('Any class inheriting FSDuplicate should implement their own data property')

    def fs_dump(self):
        if not os.path.exists(self.fs_path):
            os.makedirs(self.fs_path)
        with open(self.fs_full_path, 'w') as f:
            f.write(self.data)
        return
