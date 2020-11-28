# データベース管理ツールから編集できるようにする設定
from django.contrib import admin

from .models import Friend
# Register your models here.

admin.site.register(Friend)
