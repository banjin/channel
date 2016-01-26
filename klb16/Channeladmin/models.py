from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='Email', max_length=255)

    def __unicode__(self):
        return self.username
