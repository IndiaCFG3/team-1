from django.contrib import admin
from . models import users,Course

admin.register(Course)
admin.site.register(users)

