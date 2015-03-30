from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase

from .test_views import setup_models


class SoloAPITestCase(APITestCase):

    def setUp(self):
        setup_models(self)

    def test_create_solo(self):
        """ Test that we can create a solo
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
            'url': 'http://testserver/api/solos/3/',
            'artist': 'John Coltrane',
            'slug': 'john-coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21',
            'track': 'http://testserver/api/tracks/2/'
        })

    def test_solo_create_route(self):
        """ Test that we've got routing set up for Solos
        """
        route = resolve('/api/solos/')

        self.assertEqual(route.func.__name__, 'SoloViewSet')
