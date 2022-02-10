from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    phonenumber = models.IntegerField()
    designation  = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='images/',default='SOME STRING')
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)

class UserApplyLeave(models.Model):
    leavetype = models.CharField(max_length=200)
    fromdate = models.DateField(blank=True, null=True)
    to = models.DateField(blank=True, null=True)
    daytype = models.CharField(max_length=200,null=True, blank=True)
    session = models.CharField(max_length=200, null=True, blank=True)
    reason = models.CharField(max_length=500)
    user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)