from rest_framework import serializers
from .models import YouTubeVideo

from langserve import RemoteRunnable
from pytube import YouTube

class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = [
            'id',
            'video_id',
            'title',
            'description',
            'duration',
            'thumbnail_url',
            'created_at',
            'updated_at',
            'summary',
        ]
        read_only_fields = ['title', 'description', 'duration', 'thumbnail_url', 'summary']

    def create(self, validated_data):
        video_id = validated_data.get('video_id')
        additional_data = self.get_video_info(video_id)
        validated_data.update(additional_data)
        return super().create(validated_data)

    def get_video_info(self, video_id):
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        remote_chain = RemoteRunnable("http://localhost:8001/youtube-summary/")
        
        yt = YouTube(youtube_url)
        summary = remote_chain.invoke(youtube_url)

        return {
            'title': yt.title,
            'description': yt.description,
            'duration': yt.length,
            'thumbnail_url': yt.thumbnail_url,
            'summary': summary
        }