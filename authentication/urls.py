from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.views import signup

urlpatterns = [
    path("", signup, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="authentication/logout.html"), name="logout"),
    ]