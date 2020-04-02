from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('test', views.landing_test, name='landing-test'),
]
