from django.urls import path
from . import views

app_name='toys'
urlpatterns = [
    path('', views.dashboard, name='dashboard')
]
