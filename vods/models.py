from django.conf import settings
from django.db import models


class GameDetails(models.Model):
    map = models.CharField(max_length=200, choices=settings.MAP_CHOICES)
    winning_team = models.CharField(max_length=10, choices=settings.TEAM_CHOICES)
    length = models.IntegerField()
    vod = models.ForeignKey("vods.Vod", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vod.title} - {self.map} - {self.winning_team} - {self.length} seconds"

    class Meta:
        verbose_name_plural = "Game Details"


class Vod(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to="videos/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Users can upload their own vods.
    belongs_to = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    # However, if a vod is played by player who does not have an account, we still attribute it appropriately.
    played_by = models.CharField(unique=False, max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=50, choices=settings.TAG_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title
