from django.contrib import admin
from . models import users,Course,video,Question

admin.site.register(users)
admin.site.register(Course)
admin.site.register(video)
admin.site.register(Question)

