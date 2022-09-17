from django.urls import path

from products.views import BookViewSet


urlpatterns = [
    path('books/', BookViewSet.as_view()),
    path('books/<int:pk>/', BookViewSet.as_view())
]
