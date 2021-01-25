from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listings),
    path('listings/', views.listings, name='listings')
]
