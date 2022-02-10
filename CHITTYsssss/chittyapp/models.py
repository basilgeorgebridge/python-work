from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.IntegerField(null = True)
    idproof = models.ImageField(null=True,upload_to = "img/",blank=True)

    def __unicode__(self):
        return self.username

