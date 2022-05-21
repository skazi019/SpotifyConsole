from django.db import models


# Create your models here.
class SpotifyTokens(models.Model):
    sesssionkey = models.CharField(max_length=100)
    access_token = models.CharField(max_length=150)
    refresh_token = models.CharField(max_length=150)
    expires = models.DateTimeField()
    profile_data = models.JSONField(default=dict)
    top_artists_short = models.JSONField(default=dict)
    top_artists_medium = models.JSONField(default=dict)
    top_artists_long = models.JSONField(default=dict)
    top_tracks_short = models.JSONField(default=dict)
    top_tracks_medium = models.JSONField(default=dict)
    top_tracks_long = models.JSONField(default=dict)
    userid = models.CharField(max_length=255, default="Anonymous")

    def __str__(self):
        return f"{self.sesssionkey} | {self.expires} | {self.profile_data} | {self.top_artists_long} | {self.top_tracks_long}"
