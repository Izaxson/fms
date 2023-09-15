from django.urls import path
from django.views import View
from account import auth_views

urlpatterns = [
 path('', auth_views.user_login, name='login'),
 path('logout/', auth_views.user_logout, name='logout'),
#  path('login/', auth_views.LoginView.as_view(), name='login'),
#  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]