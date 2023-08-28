from django.urls import include, path
from .views import *


urlpatterns = [
    path('send', send_message),
]
