from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(UserOTP)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(Dislike)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Post)




