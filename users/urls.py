from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verify, ResetPasswordView, NewPassGenerateView, NewEmailVerify, \
    UserListView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/<str:token>', verify, name='verify'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('new_pass_generate/', NewPassGenerateView.as_view(), name='new_pass_generate'),
    path('email_verify', NewEmailVerify.as_view(), name='new_email_verify'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('moderator/user_edit/<int:pk>', UserUpdateView.as_view(), name='user_edit')
]
