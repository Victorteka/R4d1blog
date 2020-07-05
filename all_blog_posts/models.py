from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime


# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = RichTextUploadingField(blank=True)
