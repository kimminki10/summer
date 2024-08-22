# youtube/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from youtube import views

app_name = 'youtube'

urlpatterns = [
    path('youtube/', views.YouTubeVideoList.as_view()),
    path('youtube/<int:pk>/', views.YouTubeVideoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)