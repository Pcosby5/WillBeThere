from django.urls import path
from .import views
from knox.views import LogoutView, LogoutAllView
from .views import UserListView, UserDetailView, UserDeleteView
from .views import GetProfile


urlpatterns = [
    path('profile/', GetProfile.as_view(), name='profile'),
    path('login/', views.LoginAPIView.as_view()),
    path('update-user/<uuid:pk>/', views.UpdateUserAPI.as_view()),
    path('user/delete/<uuid:id>/', UserDeleteView.as_view(), name='user-delete'),
    path('users/<uuid:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', views.RegisterUserAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
