from django.urls import path
from .import views
from knox.views import LogoutView, LogoutAllView
from .views import UserListView, UserDetailView, UserUpdateApiView, UserDeleteApiView
from .views import GetProfile
from .views import ForgotPasswordView
from .views import ChangePasswordView


urlpatterns = [
    path('profile/', GetProfile.as_view(), name='profile'),
    path('login/', views.LoginAPIView.as_view()),
    path('users/update/', UserUpdateApiView.as_view()),
    path('users/delete/', UserDeleteApiView.as_view(), name='user-delete'),
    path('users/<uuid:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', views.RegisterUserAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]
