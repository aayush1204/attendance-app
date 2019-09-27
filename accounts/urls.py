from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
   path('register/',views.register, name="register_url"),
   path('login/',LoginView.as_view(),name="login_url"), 
   # path('register/login/',LoginView.as_view(),name="login_url"), 
   path('logout/',LogoutView.as_view(next_page='login_url'),name="logout"),
]