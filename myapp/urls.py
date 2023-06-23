from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_page, name="home"),
    path('login/', views.Login_page, name="login"),
    path('upload/', views.upload_view, name="upload"),  # Include the username parameter in the URL pattern
    path('upload_req/', views.upload_req, name="upload_req"),
    path('login/', views.login_view, name='auth-login'),
    path('logout/', views.logout_view, name='logout'),
]

