from django.db import models

# Create your models here.


class ShortUrl(models.Model):
    guid = models.BigIntegerField(primary_key=True)
    short_url = models.CharField(max_length=100)
    original_url = models.CharField(max_length=2083)
    
