from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('comics/', views.ComicBookList.as_view(), name='comicbook_list'),
    path('comics/<int:pk>', views.ComicBookDetail.as_view(), name='comicbook_detail')
]
