from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'mainpage'

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainpage'),
    path('project_<project_id>/', views.GroupList.as_view(), name='grouplist'),
    path('project_<project_id>/invite', views.InviteMembers.as_view(), name='invite'),
    path('project_<project_id>/creategroup', views.CreateGroup.as_view(), name='create_group'),
    path('notice/notice', views.Notify.as_view(), name='notify'),
    path('notice/notice/approve', views.Accept.as_view(), name='accept'),
    path('notice/notice/reject', views.Reject.as_view(), name='reject'),
    path('createproject/', views.CreateProject.as_view(), name='create_project'),
    #path('/notice/delete', views.Delete.as_view(), name='delete'),
    # グループページに飛ばすために、ここでgrouppageをインクルードしている
    path('project_<project_id>/grouppage', include('grouppage.urls'))
]