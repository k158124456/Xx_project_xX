from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Group)
admin.site.register(ProjectMember)
admin.site.register(Status)
admin.site.register(Invite)
admin.site.register(Chat)
admin.site.register(Status_detail)
admin.site.register(LogAll)


# Register your models here.
