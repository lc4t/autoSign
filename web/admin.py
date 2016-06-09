from django.contrib import admin

from .models import user, banIp, signLog

admin.site.register(user)
admin.site.register(banIp)
admin.site.register(signLog)
