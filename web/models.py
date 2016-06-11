from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class users(AbstractUser):
    # user = models.ForeignKey(User,unique=True)
    # email = models.EmailField(max_length = 200, unique = True)
    # registTime = models.DateTimeField(null = True)
    registIp = models.CharField(max_length = 15, null = True)
    loginTimes = models.IntegerField(default = 0)
    lastLoginIp = models.CharField(max_length = 15, null = True)
    # lastLoginTime = models.DateTimeField(null = True)
    ban = models.BooleanField(default = False)

    def __str__(self):
        return ("%d -> %s -> %s" % (self.id, self.username, self.email))
    class Admin:
        list_display = ("id", "username", "email", "is_active", "ban", "last_login", "lastLoginIp", "loginTimes")
    class Meta:
        ordering = ["id"]

class banIp(models.Model):
    Ip = models.CharField(max_length = 15, db_index = True)
    todayLoginTimes = models.IntegerField(default = 0)

    def __str__(self):
        return ("%s login %d times today" % (self.Ip, self.todayLoginTimes))
    class Admin:
        list_display = ("Ip", "todayLoginTimes")
    class Meta:
        ordering = ["Ip"]

class script(models.Model):
    check = models.BooleanField(default = False)
    name = models.CharField(max_length = 255, default = None)
    target = models.CharField(max_length = 255, default = None)
    intro = models.CharField(max_length = 255, null = True)
    time = models.DateTimeField(default = None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    FILE = models.FileField(upload_to="scripts")
    disable = models.BooleanField(default = False)
    opened = models.BooleanField(default = True)

    def __str__(self):
        return ("[%s&%s]%s -> %s by %s @%s" % (str(self.check), (str(not self.disable)), self.name, self.target, self.author.username, str(self.time)))
    class Admin:
        list_display = ("check", "name", "target", "intro", "time", "author")
    class Meta:
        ordering = ["check", "target", "time", "author", "name"]

class task(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, to_field = 'username', on_delete = models.CASCADE, db_index = True, default = '')
    script = models.ForeignKey(script)
    status = models.BooleanField(default = True)
    message = models.CharField(null = True, max_length = 255)
    startTime = models.DateTimeField(default = None)
    def __str__(self):
        return ("[%s]%s -> %s message @%s" % (str(self.status), self.username, self.script, self.message))
    class Admin:
        list_display = ("username", "script", "status", "message")
    class Meta:
        ordering = ["status", "username", "script"]


class signLog(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, to_field = 'username', on_delete = models.CASCADE, db_index = True, default = '')
    script = models.ForeignKey(script, on_delete = models.CASCADE)
    startTime = models.DateTimeField(default = None)
    endTime = models.DateTimeField(default = None)
    status = models.BooleanField()
    message = models.TextField(null = True)

    def __str__(self):
        return ("[%s]%s -> %s start @%s" % (str(self.status), self.username, self.script, str(self.startTime)))
    class Admin:
        list_display = ("username", "script", "startTime", "endTime", "status", "message")
    class Meta:
        ordering = ["username", "script", "startTime"]
