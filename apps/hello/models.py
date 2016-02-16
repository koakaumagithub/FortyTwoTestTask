from django.db import models

class Info(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    bio   = models.TextField()
    def __unicode__(self):
        return self.title
