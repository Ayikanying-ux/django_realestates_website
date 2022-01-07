from django.urls import path

from core.views import AddLike, post_comments, detail_page, homepage

urlpatterns = [
    path("", homepage, name="homepage"),
    path("detail/<str:pk>/", detail_page, name="detail"),
    path('<str:pk>/', AddLike.as_view(), name="like_estate"),
    path('detail/<str:pk>/comments/', post_comments, name="comments"),
]