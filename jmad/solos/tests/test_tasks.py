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

