from unittest.mock import patch

from django.test import TestCase

from solos.tasks import get_artist_tracks_from_musicbrainz


class SoloTaskTestCase(TestCase):

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
                    'id': '46a6fac0-2e14-4214-b08e-3bdb1cffa5aa',
                    'tag-list': [
                        {'count': '1', 'name': 'jazz fusion'},
                        {'count': '1', 'name': 'bassist'}
                    ]
                }
            ]
        }

        recording1 = {
            'recording': {
                'id': '12348765-4321-1234-3421-876543210921',
                'title': 'Donna Lee',
            },
            'position': '1'
        }

        recording2 = {
            'recording': {
                'id': '15263748-4321-8765-8765-102938475610',
                'title': 'Sophisticated Lady',
            },
            'position': '6'
        }

        mock_mb_browse_releases.return_value = {
            'release-list': [
                {
                    'title': 'Jaco Pastorius',
                    'id': '876543212-4321-4321-4321-21987654321',
                    'medium-list': [
                        {
                            'track-list': [recording1]
                        }
                    ]
                },
                {
                    'title': 'Invitation',
                    'id': '43215678-5678-4321-1234-901287651234',
                    'medium-list': [
                        {
                            'track-list': [recording2]
                        }
                    ]
                }
            ]
        }


        created_solos = get_artist_tracks_from_musicbrainz('Jaco Pastorius')

        mock_mb_search_artists.assert_called_with('Jaco Pastorius')
        self.assertEqual(len(created_solos), 2)
        self.assertEqual(created_solos[0].artist, 'Jaco Pastorius')
        self.assertEqual(created_solos[1].track.name, 'Donna Lee')
