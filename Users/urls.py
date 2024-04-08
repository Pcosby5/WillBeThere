from django.urls import path
# from Users import views as user_views
from django.contrib.auth import views as auth_views
from .views import UserRegisterView
from .views import CustomLogoutView
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.auth.views import LogoutView
# from .views import register, user_login, user_logout

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
