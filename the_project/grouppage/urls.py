from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "roompage"

urlpatterns = [
    # ここに再接続された地点でmainpage/<projectname>/grouppage/はくっついてる
    path("", views.RoomPage.as_view(), name="roompage"),
    path("group_settings/",views.Group_settings.as_view(),name="group_settings"),
    path("status_edit/",views.Status_new.as_view(),name="status_new"),
    path("group_namechange/",views.Group_NameChange.as_view(),name="group_namechange"),
    path("group_delete/",views.Group_Delete.as_view(),name="group_delete"),
    path("group_delete_complete/",views.Group_Delete_Complete.as_view(),name="group_delete_complete"),
]