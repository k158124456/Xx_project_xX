from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "grouppage"

urlpatterns = [
    # ここに再接続された地点でmainpage/<projectname>/grouppage/はくっついてる
    path("", views.RoomPage.as_view(), name="grouppage")
]