from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import RegisterUserView
urlpatterns = [
    path('users_register/', RegisterUserView.as_view(), name='register_user'),
    path('users_login/', LoginView.as_view(template_name = "users/login.html"), name='login_user'),
    path('users_logout/', LogoutView.as_view(), name='logout')
]