from django.test import TestCase

from solos.models import Solo


class SoloModelTestCase(TestCase):

    def setUp(self):
        self.solo = Solo.objects.create(
            track='Falling in Love with Love',
            artist='Peterson',
            instrument='guitar',
            album='The Oscar Peterson Trio at the Stratford Shakespearean Festival',
            start_time='1:24',
            end_time='4:06'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Peterson')
        self.assertEqual(self.solo.end_time, '4:06')
