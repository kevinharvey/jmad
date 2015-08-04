from django.test import TestCase

from vcr import VCR

from solos.tasks import get_artist_tracks_from_musicbrainz


albums_vcr = VCR(cassette_library_dir='albums/tests/vcr_cassettes')

class SoloTaskTestCase(TestCase):

    def test_get_artist_tracks_from_musicbrainz(self):
        """
        Test that we can make Solos from the MusicBrainz API
        """
        with albums_vcr.use_cassette('search-jaco-pastorius.yml'):
            created_solos = get_artist_tracks_from_musicbrainz('Jaco Pastorius')

        self.assertEqual(len(created_solos), 192)
        self.assertEqual(created_solos[0].artist, 'Jaco Pastorius')
        self.assertEqual(created_solos[1].track.name, 'The High and the Mighty / If You Could See Me Now')

    def test_slugify_max_length(self):
        """
        Test that we can handle slugifying track titles that are longer than 50 chars
        """
        with albums_vcr.use_cassette('search-oscar-peterson.yml'):
            queryset = get_artist_tracks_from_musicbrainz('Oscar Peterson')

        self.assertEqual(queryset.count(), 236)

    def test_reject_non_jazz_artists(self):
        """
        Test that we do not add non-jazz artists when searched for
        """
        with albums_vcr.use_cassette('search-nirvana.yml'):
            queryset = get_artist_tracks_from_musicbrainz('Nirvana')

        self.assertEqual(queryset.count(), 0)

    def test_instrument_tag_map(self):
        """
        Test that we set instrument to 'unknown' if we do not have a reliable mapping for MB tags to jazz instruments
        """
        with albums_vcr.use_cassette('search-miles-davis.yml'):
            queryset = get_artist_tracks_from_musicbrainz('Miles Davis')

        self.assertEqual(queryset[0].instrument, 'unknown')
