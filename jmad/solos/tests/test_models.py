from unittest.mock import patch

from django.test import TestCase

from solos.models import Solo
from albums.models import Album, Track


class SoloModelTestCase(TestCase):

    def setUp(self):

        self.album = Album.objects.create(
            name='At the Stratford Shakespearean Festival',
            artist='Oscar Peterson Trio',
            slug='at-the-stratford-shakespearean-festival'
        )
        self.album.save()

        self.track = Track.objects.create(
            name='Falling in Love with Love',
            album=self.album,
            track_number=1,
            slug='falling-in-love-with-love'
        )
        self.track.save()

        self.solo = Solo.objects.create(
            track=self.track,
            artist='Oscar Peterson',
            instrument='guitar',
            start_time='1:24',
            end_time='4:06',
            slug='oscar-peterson'
        )
        self.solo.save()

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
        self.assertEqual(self.solo.end_time, '4:06')

    def test_get_absolute_url(self):
        """
        Test that we can build a URL for a solo
        """
        self.assertEqual(
            self.solo.get_absolute_url(),
            '/recordings/at-the-stratford-shakespearean-festival/falling-in-love-with-love/oscar-peterson/'
        )

    @patch('musicbrainzngs.browse_releases')
    @patch('musicbrainzngs.search_artists')
    def test_get_artist_tracks_from_musicbrainz(self, mock_mb_search_artists, mock_mb_browse_releases):
        """
        Test that we can make Solos from the MusicBrainz API
        """
        mock_mb_search_artists.return_value = {
            'artist-list': [
                {
                    'name': 'Jaco Pastorius',
                    'ext:score': '100',
                    'id': '12345678-1234-1234-1234-123456789012'
                }
            ]
        }
        mock_mb_browse_releases.return_value = {
            'release-list': [
                {
                    'title': 'Jaco Pastorius',
                    'id': '876543212-4321-4321-4321-21987654321',
                    'medium-list': [
                        {
                            'track-list': [
                                {
                                    'recording': {
                                        'id': '12348765-4321-1234-3421-876543210921',
                                        'title': 'Donna Lee',
                                    },
                                    'position': '1'
                                }
                            ]
                        }
                    ]
                },
                {
                    'title': 'Invitation',
                    'id': '43215678-5678-4321-1234-901287651234',
                    'medium-list': [
                        {
                            'track-list': [
                                {
                                    'recording': {
                                        'id': '15263748-4321-8765-8765-102938475610',
                                        'title': 'Sophisticated Lady',
                                    },
                                    'position': '6'
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        created_solos = Solo.get_artist_tracks_from_musicbrainz('Jaco Pastorius')

        mock_mb_search_artists.assert_called_with('Jaco Pastorius')
        mock_mb_browse_releases.assert_called_with('12345678-1234-1234-1234-123456789012', includes=['recordings'])
        self.assertEqual(len(created_solos), 2)
        self.assertEqual(created_solos[0].artist, 'Jaco Pastorius')
        self.assertEqual(created_solos[1].track.name, 'Donna Lee')
