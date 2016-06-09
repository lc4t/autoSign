from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class user(AbstractBaseUser):
    email = models.EmailField(max_length = 200, unique = True)
    registTime = models.DateTimeField()
    registIp = models.CharField(max_length = 15, null = True)
    loginTimes = models.IntegerField(default = 0)
    lastLoginIp = models.CharField(max_length = 15, null = True)
    lastLoginTime = models.DateTimeField()
    ban = models.BooleanField(default = False)

class banIp(models.Model):
    Ip = models.CharField(max_length = 15, db_index = True)
    todayLoginTimes = models.IntegerField(default = 0)

class signLog(models.Model):
    email = models.OneToOneField(user, to_field = 'email', on_delete = models.CASCADE)
    script = models.CharField(max_length = 255)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    status = models.BooleanField()
    message = models.TextField(null = True)
