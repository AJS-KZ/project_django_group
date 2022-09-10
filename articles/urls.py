from rest_framework.routers import DefaultRouter
from django.urls import path

from articles.views import ArticleViewSet, ArticleFileViewSet


router = DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path('files/', ArticleFileViewSet.as_view()),
    path('files/<int:pk>/', ArticleFileViewSet.as_view())
] + router.urls
