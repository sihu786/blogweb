from django.contrib import admin

from .models import User # custom user model

# Register your models here.

admin.site.register(User)