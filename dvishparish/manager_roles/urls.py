from django.urls import path

from dvishparish.manager_roles import views

app_name = "manager_roles"

urlpatterns = [
    path("", views.IndexManagerView.as_view(), name="index"),
    path("plans/manager/", views.ManagerPlansView.as_view(), name="manager_plans"),
    path("plans/bankoffice/", views.BankOfficePlansView.as_view(), name="manager_bankoffice_plans"),

]
