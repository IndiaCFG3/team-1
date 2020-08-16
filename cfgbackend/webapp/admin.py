from django.contrib import admin
from . models import users,Course,video,Question

admin.register(Course)
admin.site.register(users)
admin.site.register(video)
admin.site.register(Question)

