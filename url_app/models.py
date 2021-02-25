from django.db import models


# Create your models here.

class ShortUrl(models.Model):
    url = models.CharField(max_length=256)
    slug = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return f'{self.url}'
