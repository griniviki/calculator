
# calculator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallpaper_calculator_view, name='wallpaper_calculator'),
]

