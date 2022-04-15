from django.contrib import admin

from .models import Search, User

# Register your models here.

admin.site.register(User)
admin.site.register(Search)