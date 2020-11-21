from django.urls import path, include

print(path("app1/", include("app1.urls")))