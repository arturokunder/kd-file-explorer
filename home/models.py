from django.contrib.auth.models import User
from django.db import models

class Permission(models.Model):
    user = models.OneToOneField(User)
    folder = models.CharField(max_length=244, null=False)

    def __unicode__(self):
        return self.user.username + ' ' + self.user.first_name + ' ' + self.user.last_name + ' ' + self.folder
