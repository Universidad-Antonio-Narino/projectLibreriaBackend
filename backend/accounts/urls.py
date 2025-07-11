from django.urls import path
from .views import *

urlpatterns = [
    path('api/register/',RegisterView.as_view(),name="user_register"),
    path('api/login/',LoginView.as_view(),name="user_login"),
    path('api/logout/',LogoutView.as_view(),name="user_logout")
]