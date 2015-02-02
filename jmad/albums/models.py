from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Track(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album)
    track_number = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['album', 'track_number']
