from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    # Core User Routes
    path('', views.landing_page, name='landing'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Profile Management
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/delete/', views.delete_account_view, name='delete_account'),

    # Payment Routes
    path('pay/', views.create_order, name='payment'),
    path('checkout/', views.payment_checkout, name='payment_checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('error/', views.payment_error, name='payment_error'),

    
    # Password Management
    path('profile/change-password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url=reverse_lazy('password_change_done')  # ✅ This uses the named URL
    ), name='change_password'),

    path('profile/change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/change_password_done.html'
    ), name='password_change_done'),
    # Forgot Password (Custom, No Email)
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
]
