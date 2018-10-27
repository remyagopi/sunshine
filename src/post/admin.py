from django.contrib import admin

from .models import Post

from django.contrib.auth.models import Group


admin.site.register(Post)

admin.site.unregister(Group)


