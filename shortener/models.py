from django.db import models

# Create your models here.


class ShortUrl(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, unique=True)
    short_url = models.CharField(max_length=20)
    original_url = models.CharField(max_length=2083)
    
