__author__ = 'Matthew'

import re
from django.core.exceptions import ValidationError


def validate_handle(value):
    if not value.startswith('/pages/'):
        raise ValidationError('Page handle should always start with "/pages/" followed by one or more tail components.')
    elif len(value) <= len('/pages/'):
        raise ValidationError('Page handle should always have one or more tail components ending with a backslash. '
                              'Example: "/pages/tail1/.../".')
    elif not value.endswith('/'):
        raise ValidationError('Page handle should always end with a backslash ("/").')
    elif not re.match('^[/A-Za-z0-9_-]*$', value):
        raise ValidationError('Page handle can only contain alphanumeric characters and "/", "-", "_".')
