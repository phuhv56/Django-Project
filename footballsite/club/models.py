from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name