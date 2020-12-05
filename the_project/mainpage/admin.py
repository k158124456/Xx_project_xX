from django.contrib import admin
from mainpage.models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Group)
admin.site.register(ProjectMember)
admin.site.register(Status)

from .models import Invite

admin.site.register(Invite)
