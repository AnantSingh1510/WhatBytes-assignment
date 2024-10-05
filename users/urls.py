from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), #Both of these urls go to the login screen
    path('login/', views.login_view, name='login'),

    path('signup/', views.signup_view, name='signup'),

    # All of these urls need an authenticated user
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),

    # All these link are related to forgot password and therefore I have branched them together.
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='users/forgot_password.html'), name='forgot_password'),
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
