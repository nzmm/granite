from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from granite import validators
from granite.core.objects import FSDuplicate

from websites.models import Website


class Template(models.Model, FSDuplicate):
    FS_ROOT = 'pages/templates/gen'

    site = models.ForeignKey(Website)
    handle = models.CharField(max_length=48)
    markup = models.TextField(default='')

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.handle)

    @property
    def data(self):
        return self.markup


# Template signal handlers
@receiver(post_save, sender=Template)
def template_post_save_handler(sender, **kwargs):
    kwargs['instance'].fs_dump()
    return


@receiver(pre_delete, sender=Template)
def template_pre_delete_handler(sender, **kwargs):
    print(sender, kwargs)
    return


class Page(models.Model):

    NONE = 'NN'
    HOME = 'HM'
    ERROR = 'ER'

    PAGE_ROLES = (
        (NONE, 'Standard Page'),
        (HOME, 'Home Page'),
        (ERROR, 'Error Page'),
    )

    site = models.ForeignKey(Website)
    title = models.CharField(max_length=100)
    handle = models.CharField(max_length=100, default='/pages/', validators=[validators.validate_page_handle])
    page_description = models.CharField(max_length=255, blank=True, default='')
    content = models.TextField(default='')
    template = models.ForeignKey(Template)
    role = models.CharField(max_length=2, choices=PAGE_ROLES, default=NONE)
    quick_link = models.BooleanField(default=False)
    mtime = models.DateTimeField(auto_now=True)
    page_author = models.ForeignKey(User)
    published = models.BooleanField(default=True)

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.title)

    @property
    def description(self):
        def _fullstop(s):
            s = s.strip()
            if not s.endswith('.'):
                s += '.'
            return s
        return ' '.join(_fullstop(desc) for desc in (self.site.description, self.page_description))
