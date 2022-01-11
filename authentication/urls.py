from django.urls import path

from authentication.views import signup

urlpatterns = [
    path("", signup, name="register"),
    ]