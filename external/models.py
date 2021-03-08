"""Quiz models."""
from django.db import models

from imagetext.utils import image_upload_location


class Item(models.Model):
    """Store image and text pairing."""

    image = models.ImageField(upload_to=image_upload_location())
    text = models.CharField(max_length=1000)
