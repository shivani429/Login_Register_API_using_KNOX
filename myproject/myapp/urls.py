from django.contrib import admin
from django.urls import path
from myapp import views
from knox import views as konx_views
from .views import *
# from knox import views as knox_views
# from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('hi', knox_views.hi),
    # path('hello/<int:id>',knox_views.hello),
    path('login', views.login_api),
    path('user', views.get_user_data),
    path('register', views.register_api),
    path('logout', konx_views.LogoutView.as_view()),
    path('logoutall', konx_views.LogoutAllView.as_view()),
  
]
