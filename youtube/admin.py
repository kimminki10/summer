from django.contrib import admin
from .models import YouTubeVideo

class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'duration', 'created_at')
    search_fields = ('video_id', 'title')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(YouTubeVideo, YouTubeVideoAdmin)