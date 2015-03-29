from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase

from .test_views import setup_models


class SoloAPITestCase(APITestCase):

    def setUp(self):
        setup_models(self)

    def test_create_solo(self):
        """ Test that we can get a list of solos
        """
        post_data= {
            'track': '/api/tracks/2/',
            'artist': 'John Coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21'
        }
        response = self.client.post('/api/solos/', data=post_data, format='json')

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, {
            'artist': 'John Coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21',
            'track': {
                'name': 'Mr. P.C.',
                'url': 'http://jmad.us/api/tracks/2/'
            }
        })

    def test_solo_create_route(self):
        """ Test that we've got routing set up for Solos
        """
        route = resolve('/api/solos/')

        self.assertEqual(route.func.__name__, 'SoloViewSet')
