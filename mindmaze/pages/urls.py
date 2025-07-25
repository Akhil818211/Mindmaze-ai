from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('features/', views.features_view, name='features'),
    path('blog/', views.blog_view, name='blog'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_view, name='terms'),
    path('cookie-policy/', views.cookie_policy_view, name='cookie_policy'),
    path('faq/', views.faq_view, name='faq'),


]
