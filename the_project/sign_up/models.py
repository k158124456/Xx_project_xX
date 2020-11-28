from django.db import models

# Create your models here.

class UserList(models.Model):
    user_id = models.CharField(max_length=20)
    mail = models.EmailField(max_length=100)
    pswd = models.CharField(max_length=20)
