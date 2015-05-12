from django.db import models
from django.core.urlresolvers import reverse

from albums.models import Track


class Solo(models.Model):
    track = models.ForeignKey(Track)
    artist = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('solo_detail_view', kwargs={'album': self.track.album.slug, 'track': self.track.slug,
                                                   'artist': self.slug})
