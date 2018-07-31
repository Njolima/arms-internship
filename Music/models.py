from django.db import models

app_name = 'Music'


class Album(models.Model):
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=230)
    artist = models.CharField(max_length=190)

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    category = models.ForeignKey(Album, on_delete=models.CASCADE, default=True)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title
