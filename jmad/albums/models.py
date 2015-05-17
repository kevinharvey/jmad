from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100) 
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album)
    track_number = models.PositiveIntegerField(blank=True, null=True) 
    slug = models.SlugField()

    class Meta:
        ordering = ['album', 'track_number']

    def __str__(self):
        return self.name
