from django.contrib import admin
from django.urls import path, include

from .views import hello

urlpatterns = [
    path('', hello),
    path('admin/', admin.site.urls),
    path('', include('youtube.urls')),
]
