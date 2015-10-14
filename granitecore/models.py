from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class Asset(models.Model):
    name = models.CharField(max_length=48)
    file = models.FileField(upload_to='assets')


class Website(models.Model):
    name = models.CharField(max_length=100)
    favicon = models.ForeignKey(Asset, blank=True, null=True, related_name='favicons')
    brand_small = models.ForeignKey(Asset, blank=True, null=True, related_name='branding_small')
    brand_medium = models.ForeignKey(Asset, blank=True, null=True, related_name='branding_medium')
    brand_large = models.ForeignKey(Asset, blank=True, null=True, related_name='branding_large')
    brand_original = models.ForeignKey(Asset, blank=True, null=True, related_name='branding_original')

    def __str__(self):
        return self.name


class Template(models.Model):
    site = models.ForeignKey(Website)
    name = models.CharField(max_length=48)
    text = models.TextField(default='')

    def __str__(self):
        return "%s/%s" % (self.site.name.replace(' ', '_'), self.name)

    @property
    def fs_path(self):
        return "granitecore/templates/gen/%s" % self.site.name.replace(' ', '_')

    @property
    def fs_name(self):
        return "%i_%s" % (int(self.pk), self.name)


class Page(models.Model):
    site = models.ForeignKey(Website)
    title = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    content = models.TextField(default='')
    template = models.ForeignKey(Template)
    visible = models.BooleanField(default=True)
    mtime = models.DateTimeField(auto_now=True)
    mauthor = models.ForeignKey(User)
    published = models.DateTimeField(blank=True)
    publish_at = models.DateTimeField(blank=True)
    unpublish_at = models.DateTimeField(blank=True)

    def __str__(self):
        return "//%s/%s" % (self.site.name.replace(' ', '_'), self.title)


# Signal handlers
@receiver(post_save, sender=Template)
def template_post_save_handler(sender, **kwargs):
    print(sender, kwargs)
    import os
    print(os.getcwd())
    template = kwargs['instance']

    if not os.path.exists(template.fs_path):
        os.makedirs(template.fs_path)

    outfile = os.path.join(template.fs_path, template.fs_name)
    with open(outfile, 'w') as f:
        f.write(template.text)
    return


@receiver(pre_delete, sender=Template)
def template_post_delete_handler(sender, **kwargs):
    print(sender, kwargs)
    return
