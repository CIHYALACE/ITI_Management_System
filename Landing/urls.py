from django.urls import path
from Landing.views import LandingPage


urlpatterns = [
    path('', LandingPage, name='LandingPage'),
]