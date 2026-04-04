from . import views
from django.urls import path

app_name = "mainApp"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('terms/', views.terms_view, name='terms'),
]
