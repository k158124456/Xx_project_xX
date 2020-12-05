from django.db import models
from sign_up.models import *
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    #project_id=models.CharField(max_length=100,primary_key=True)
    project_name=models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

class Group(models.Model):
    #group_id=models.CharField(max_length=100,primary_key=True)
    project_id=models.ForeignKey(Project, on_delete=models.CASCADE)
    group_name=models.CharField(max_length=100)
    #image=

    def __str__(self):
        return self.group_name

class ProjectMember(models.Model):
    userlist = models.ForeignKey(User, on_delete=models.CASCADE)
    projectlist = models.ForeignKey(Project, on_delete=models.CASCADE)
    displayname=models.CharField(max_length=100)
    role=models.IntegerField(max_length=3)
    def __str__(self):
        return str(self.userlist) + "," + str(self.projectlist) + "," + str(self.displayname) + "," + str(self.role)

class Status(models.Model):
    group_id=models.ForeignKey(Group, on_delete=models.CASCADE)
    userlist = models.ForeignKey(User, on_delete=models.CASCADE)
    status= models.IntegerField(max_length=3)

    def __str__(self):
        return str(self.group_id)+","+str(self.userlist)+","+str(self.status)



