from .views import LogoutView,  LoginView
from django.urls import  path

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Other URL patterns go here
  
]