from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "roompage"

urlpatterns = [
    # ここに再接続された地点でmainpage/<projectname>/grouppage/はくっついてる
    path("", views.RoomPage.as_view(), name="roompage"),
    path("status_edit/",views.Status_new.as_view(),name="status_new"),
    path("group_settings/",views.Group_settings.as_view(),name="group_settings"),
]