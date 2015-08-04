from django.utils.text import slugify

from celery import shared_task
import musicbrainzngs as mb

from .models import Solo
from albums.models import Album, Track


mb.set_useragent('JMAD - https://jmad.us/', version='0.0.1')


@shared_task
def get_artist_tracks_from_musicbrainz(artist):
    """
    Create Album, Track, and Solo records for artists we find in the MusicBrainzNGS API

    :param artist: an artist's name as a string to search for
    :return: Queryset of Solos
    """
    search_results = mb.search_artists(artist)
    best_result = search_results['artist-list'][0]

    if 'jazz' not in [d['name'] for d in best_result['tag-list']]:
        return Solo.objects.none()

    instrument = Solo.get_instrument_from_musicbrainz_tags(best_result['tag-list'])

    for album_dict in mb.browse_releases(best_result['id'], includes=['recordings'])['release-list']:

        album = Album.objects.create(name=album_dict['title'], artist=artist, slug=slugify(album_dict['title']))

        for track_dict in album_dict['medium-list'][0]['track-list']:
            track = Track.objects.create(album=album, name=track_dict['recording']['title'],
                                         track_number=track_dict['position'],
                                         slug=slugify(track_dict['recording']['title']))

            Solo.objects.create(track=track, artist=artist, instrument=instrument, slug=slugify(artist))

    return Solo.objects.filter(artist=artist)
