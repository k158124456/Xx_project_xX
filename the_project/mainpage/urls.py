from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'mainpage'

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainpage'),
    path('project_<project_id>/', views.GroupList.as_view(), name='grouplist'),
    path('project_<project_id>/invite', views.InviteMembers.as_view(), name='invite'),
    path('project_<project_id>/creategroup', views.CreateGroup.as_view(), name='create_group'),
    path('project_<project_id>/setting', views.ProjectSettings.as_view(), name='project_settings'),
    path('project_<project_id>/setting/namesetting', views.ProjectSettings_nemesetting.as_view(), name='project_settings_namesetting'),
    path('project_<project_id>/setting/display_name', views.ProjectSettings_display_name.as_view(), name='project_settings_display_name'),
    path('project_<project_id>/setting/member', views.ProjectSettings_member.as_view(), name='project_settings_member'),
    path('project_<project_id>/setting/delete', views.ProjectSettings_delete.as_view(), name='project_settings_delete'),
    path('project_<project_id>/setting/delete/verification', views.ProjectSettings_delete_verification.as_view(), name='project_settings_delete_verification'),
    path('project_<project_id>/setting/delete/complete', views.ProjectSettings_delete_complete.as_view(), name='project_settings_delete_complete'),
    path('notice/', views.Notify.as_view(), name='notify'),
    path('notice/notice/approve', views.Accept.as_view(), name='accept'),
    path('notice/notice/reject', views.Reject.as_view(), name='reject'),
    path('createproject/', views.CreateProject.as_view(), name='create_project'),
    #path('/notice/delete', views.Delete.as_view(), name='delete'),
    # グループページに飛ばすために、ここでgrouppageをインクルードしている
    path('project_<project_id>/grouppage_<group_id>/', include('grouppage.urls')),
    
]