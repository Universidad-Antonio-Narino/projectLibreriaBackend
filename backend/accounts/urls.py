from django.urls import path
from .views import *

urlpatterns = [
    path('api/register/',Record.as_view(),name="user_register"),
    path('api/login/',Login.as_view(),name="user_login"),
]