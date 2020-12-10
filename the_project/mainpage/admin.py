from django.contrib import admin
from .models import *
from .models import Invite

admin.site.register(Project)
admin.site.register(Group)
admin.site.register(ProjectMember)
admin.site.register(Status)




admin.site.register(Invite)
# Register your models here.
