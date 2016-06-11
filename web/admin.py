from django.contrib import admin

from .models import users, banIp, signLog, script, task

admin.site.register(users)
admin.site.register(banIp)
admin.site.register(signLog)
admin.site.register(script)
admin.site.register(task)
