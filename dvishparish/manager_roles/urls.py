from django.urls import path

from dvishparish.manager_roles import views

app_name = "manager_roles"

urlpatterns = [
    path("", views.IndexManagerView.as_view(), name="index"),
]
