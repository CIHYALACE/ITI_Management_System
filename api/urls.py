from django.urls import path
from api.views import DjangoAPI

urlpatterns = [
    path('data', DjangoAPI, name='api'),
]
