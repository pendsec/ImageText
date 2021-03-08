"""Backend utilities."""
from django.conf import settings


def image_upload_location():
    """Image upload location."""
    if 'psu.edu' in settings.ALLOWED_HOSTS:
        return settings.STATIC_ROOT.strip('/') + "/img"

    else:
        return "static/img"
