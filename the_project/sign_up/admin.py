from django.contrib import admin
from .models import UserList 
from mainpage.models import *

# Register your models here.

admin.site.register(UserList)
admin.site.register(Project)
admin.site.register(Group)
admin.site.register(ProjectMember)
admin.site.register(Status)