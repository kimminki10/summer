from rest_framework import generics
from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer

class YouTubeVideoList(generics.ListCreateAPIView):
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer

class YouTubeVideoDetail(generics.RetrieveUpdateAPIView):
    queryset = YouTubeVideo.objects.all()
    serailizer_class = YouTubeVideoSerializer