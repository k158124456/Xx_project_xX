from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'mainpage'

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainpage'),
    path('<project_id>/', views.GroupList.as_view(), name='grouplist'),
    path('<project_id>/invite', views.InviteMembers.as_view(), name='invite'),
    path('<project_id>/create', views.CreateGroup.as_view(), name='create'),
    path('/notice', views.Notify.as_view(), name='notify'),
    # グループページに飛ばすために、ここでgrouppageをインクルードしている
    path('<project_id>/grouppage', include('grouppage.urls'))
]