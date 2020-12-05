from django.contrib import admin

admin.site.register(Project)
admin.site.register(Group)
admin.site.register(ProjectMember)
admin.site.register(Status)

from .models import Invite

admin.site.register(Invite)
# Register your models here.
