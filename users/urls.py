from django.urls import path, re_path
from users.views import home, about

urlpatterns = [
    re_path('about/', about, name='about')
]
