from django.urls import path

from dvishparish.users import views
app_name = "users"
urlpatterns = [
    path("~redirect/", view=views.user_redirect_view, name="redirect"),
    path("~update/", view=views.user_update_view, name="update"),
    path("", view=views.UserDetailView.as_view(), name="detail"),
]
