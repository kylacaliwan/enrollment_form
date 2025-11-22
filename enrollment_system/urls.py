from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('authentication:login')),  # redirect root to login
    path('online/', include('online_enrollment.urls')),
    path('auth/', include('authentication.urls', namespace='authentication')),
]
