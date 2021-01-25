from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.browse),
    path('browse/', views.browse, name='browse')
]
