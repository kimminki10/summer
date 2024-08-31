from django.db import models

class YouTubeVideo(models.Model):
    video_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True)
    thumbnail_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title