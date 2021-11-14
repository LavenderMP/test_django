from django.contrib import admin

# Register your models here.

from .models import Post, SignIn, TwoFA

admin.site.register(Post)
admin.site.register(SignIn)
admin.site.register(TwoFA)