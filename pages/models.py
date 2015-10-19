import os
import markdown
from django.db import models
from granite.settings import BASE_DIR
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from granite.core.objects import FSDuplicate
from granite import validators
from websites.models import Website


class Template(models.Model, FSDuplicate):
    TEMPLATE_REL_ROOT = 'gen'
    FS_ROOT = os.path.join(BASE_DIR, 'pages', 'templates', 'gen')

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
    content = models.TextField(default='', blank=True)
    template = models.ForeignKey(Template)
    role = models.CharField(max_length=2, choices=PAGE_ROLES, default=NONE)
    page_author = models.ForeignKey(User)
    published = models.BooleanField(default=True)
    mtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s/%s" % (self.site.handle, self.title)

    @property
    def description(self):
        def _fullstop(s):
            s = str(s).strip()
            if s and not s.endswith('.'):
                s += '.'
            return s
        return _fullstop(self.page_description) or _fullstop(self.site.description)

    @property
    def content_html(self):
        return mark_safe(markdown.markdown(self.content))
