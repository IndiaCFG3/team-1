from django.contrib import admin
from . models import users,Course

admin.site.register(users)
admin.register(Course)

