from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Group)
admin.site.register(ProjectMember)
admin.site.register(Status)
admin.site.register(Invite)
admin.site.register(Chat)
# Register your models here.
