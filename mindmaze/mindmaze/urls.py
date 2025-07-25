from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),           # Landing + Login/Register
    path('challenges/', include('challenges.urls')),
    path('progress/', include('progress.urls')),
    path('mindfulness/', include('mindfulness.urls')),
    path('', include('pages.urls')),              # Feedback, Contact, About
]
