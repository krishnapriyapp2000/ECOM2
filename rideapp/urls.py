from rest_framework import views
from .views import RegisterAPI,  LoginAPI, RiderAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('ride/',RiderAPI.as_view()),
    path('ride/<int:id>/',RiderAPI.as_view()),
    # path('ride/<int:id>/',RiderAPI.as_view()),


]

