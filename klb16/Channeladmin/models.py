from django.db import models


class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username
