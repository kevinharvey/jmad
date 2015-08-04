from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album)
    track_number = models.PositiveIntegerField(blank=True, null=True) 
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['album', 'track_number']

    def __str__(self):
        return self.name
