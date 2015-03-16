from unittest.mock import patch, Mock

from django.test import TestCase, RequestFactory, Client
from django.db.models.query import QuerySet

from solos.views import index, solo_detail
from solos.models import Solo
from albums.models import Album, Track


def setup_models(testcase):
    testcase.no_funny_hats = Album.objects.create(name='No Funny Hats', slug='no-funny-hats')
    testcase.bugle_call_rag = Track.objects.create(name='Bugle Call Rag', slug='bugle-call-rag',
                                                   album=testcase.no_funny_hats)
    testcase.drum_solo = Solo.objects.create(instrument='drums', artist='Buddy Rich',
                                             slug='buddy-rich', track=testcase.bugle_call_rag)

    testcase.giant_steps = Album.objects.create(name='Giant Steps', slug='giant-steps')
    testcase.mr_pc = Track.objects.create(name='Mr. PC', slug='mr-pc',
                                          album=testcase.giant_steps)
    testcase.bass_solo = Solo.objects.create(instrument='bass', artist='Paul Chambers',
                                             slug='paul-chambers', track=testcase.mr_pc)


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        setup_models(self)

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the correct template
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    def test_index_view_returns_solos(self):
        """
        Test that the index view will attempt to return Solos if query parameters exist
        """
        response = self.client.get('/', {'instrument': 'drums'})

        solos = response.context['solos']
        self.assertIs(type(solos), QuerySet)
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist, 'Buddy Rich')

    @patch('solos.models.Solo.get_artist_tracks_from_musicbrainz')
    def test_index_view_returns_external_tracks(self, mock_solos_get_from_mb):
        """
        Test that the index view will return artists from the MusicBrainz API if none are returned from our database
        """
        mock_solo = Mock()
        mock_solo.artist = 'Jaco Pastorius'
        mock_solos_get_from_mb.return_value = [mock_solo]

        response = self.client.get('/', {
            'instrument': 'Bass',
            'artist': 'Jaco Pastorius' # Jaco Pastorius is not currently in our database
        })

        solos = response.context['solos']
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist, 'Jaco Pastorius')


class SoloViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        setup_models(self)

    def test_basic(self):
        """
        Test that the solo view returns a 200 response, uses the correct template, and gets the right context
        """
        request = self.factory.get('/solos/no-funny-hats/bugle-call-rag/buddy-rich/')

        with self.assertTemplateUsed('solos/solo_detail.html'):
            response = solo_detail(request, album=self.no_funny_hats.slug,
                                   track=self.bugle_call_rag.slug, artist=self.drum_solo.slug)

        self.assertEqual(response.status_code, 200)
        page = response.content.decode()
        self.assertInHTML('<p id="jmad-artist">Buddy Rich</p>', page)
        self.assertInHTML('<p id="jmad-track">Bugle Call Rag [1 solo]</p>', page)
