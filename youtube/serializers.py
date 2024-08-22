from rest_framework import serializers
from .models import YouTubeVideo

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
        read_only_fields = ['created_at', 'updated_at']
