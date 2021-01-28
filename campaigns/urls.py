from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_campaigns, name='campaigns'),
    path('mine/', views.user_campaigns, name='user_campaigns'),
]
