
# newone/urls.py

from django.urls import path
from .views import shape_calculator_view

urlpatterns = [
    path('', shape_calculator_view, name='shape_calculator'),  # Note the empty path for the base URL
]


