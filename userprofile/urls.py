from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path("update/", views.update, name="update"),
    path("<slug:public_name>", views.index, name="index"),
]
