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

    class Meta:
        ordering = ['track', 'start_time']

    def get_absolute_url(self):
        return reverse('solo_detail_view', kwargs={'album': self.track.album.slug, 'track': self.track.slug,
                                                   'artist': self.slug})

    def get_duration(self):
        duration_string = ''
        if self.start_time and self.end_time:
            duration_string = '{}-{}'.format(self.start_time, self.end_time)
        return duration_string

    @classmethod
    def get_instrument_from_musicbrainz_tags(cls, tag_list):
        """
        Return a single instrument from a list of dict-tags as returned in the MusicBrainzNGS API

        :param tag_list: a list of dicts with keys 'count' and 'name'
        :return: a string
        """
        map = {
            'pianist': 'piano',
            'piano jazz': 'piano',
            'bassist': 'bass'
        }
        return map[set(map.keys()).intersection([tag['name'] for tag in tag_list]).pop()]
