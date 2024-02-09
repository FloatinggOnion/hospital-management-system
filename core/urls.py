from django.urls import path
from .views import index, hospital_list

urlpatterns = [
    path('', index, name='index'),
    path('hospitals/', hospital_list, name='hospitals'),
]