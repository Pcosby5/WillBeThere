from django.urls import path
from .import views
from knox.views import LogoutView, LogoutAllView
from .views import UserListView, UserDetailView, UserDeleteView
from .views import GetProfile
# from .views import get_all_users

urlpatterns = [
    # path('login/', views.login_api),
    path('get-profile/', GetProfile.as_view(), name='get_profile'),
    path('login/', views.LoginAPIView.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('user/delete/<int:id>/', UserDeleteView.as_view(), name='user-delete'),
    path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', views.RegisterUserAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
