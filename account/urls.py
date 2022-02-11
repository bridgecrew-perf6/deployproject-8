from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)


urlpatterns = [
    path("register/", RegistrationView.as_view()),
    path("activate/<str:email>/<str:code>/", ActivationView.as_view(), name="activate"),
    path("login/", TokenObtainPairView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
    path("logout/", LogoutView.as_view()),
]