"""Quiz models."""
from django.db import models

from imagetext.utils import image_upload_location


class Item(models.Model):
    """Store image and text pairing."""

    image = models.ImageField(upload_to=image_upload_location())


class Text(models.Model):
	"""Store text captions for an image."""

	image_id = models.ForeignKey('Item', on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
