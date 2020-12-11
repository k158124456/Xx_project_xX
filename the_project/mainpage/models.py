from django.db import models
from sign_up.models import *
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name=models.CharField(max_length=100,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    #group_id=models.CharField(max_length=100,primary_key=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id=models.ForeignKey(Project, on_delete=models.CASCADE)
    group_name=models.CharField(max_length=100,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    userlist = models.ForeignKey(User, on_delete=models.CASCADE)
    projectlist = models.ForeignKey(Project, on_delete=models.CASCADE)
    displayname=models.CharField(max_length=100,default='SOME CATEGORY')
    role=models.IntegerField(default='SOME CATEGORY')

class Status(models.Model):
    group_id=models.ForeignKey(Group, on_delete=models.CASCADE)
    userlist = models.ForeignKey(User, on_delete=models.CASCADE)
    status= models.IntegerField(default='SOME CATEGORY')

class Invite(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    invite_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invite_user')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invited_user')
    message = models.CharField(max_length=100, blank=True, default='SOME CATEGORY')
    created_at = models.DateTimeField(auto_now_add=True)