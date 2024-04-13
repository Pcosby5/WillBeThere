from django.urls import path
from .import views
from knox import views as knox_views
from .views import get_user_by_id
from .views import get_all_users

urlpatterns = [
    path('login/', views.login_api),
    path('user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('users/', get_all_users, name='get_all_users'),
    path('register/', views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
]
