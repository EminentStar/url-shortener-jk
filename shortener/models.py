from django.db import models

# Create your models here.


class ShortUrl(models.Model):
    id = models.AutoField(primary_key=True)
    short_url = models.CharField(max_length=20)
    original_url = models.CharField(max_length=2083)
