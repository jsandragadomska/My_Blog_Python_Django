from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='show_profile_page'),
    path('edit_profile/<int:pk>', EditProfilePageView.as_view(), name='edit_profile_page'),
]
