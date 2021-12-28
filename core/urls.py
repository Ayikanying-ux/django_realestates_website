from django.urls import path

from core.views import comments, detail_page, homepage

urlpatterns = [
    path("", homepage, name="homepage"),
    path("detail/<str:pk>/", detail_page, name="detail"),
    path('detail/<str:pk>/comments/', comments, name="comments")
]