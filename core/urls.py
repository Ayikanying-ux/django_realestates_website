from django.urls import path

from core.views import AddDislike, AddLike, Search, post_comments, detail_page, homepage

urlpatterns = [
    path("", homepage, name="homepage"),
    path("detail/<str:pk>/", detail_page, name="detail"),
    path('detail/<str:pk>/like', AddLike.as_view(), name="like_estate"),
    path('detail/<str:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('detail/<str:pk>/comments/', post_comments, name="comments"),
    path('search/', Search.as_view(), name="search"),
]