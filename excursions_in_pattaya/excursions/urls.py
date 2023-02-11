from django.urls import path
from .views import excursion_list

urlpatterns = [
    path('', excursion_list, name='excursion_list'),
]
