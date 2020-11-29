from django.urls import path

from dvishparish.manager_roles import views

app_name = "manager_roles"

urlpatterns = [
    path(r"KPIs/", views.ManagerKPIsView.as_view(), name="self_kpis"),
    path(r"top5/", views.Top5ManagersView.as_view(), name="top_managers"),
]
