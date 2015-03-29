from unittest import TestCase

from solos.serializers import SoloSerializer


class SoloSerializerTestCase(TestCase):

    def test_validate(self):
        """ Tests that SoloSerializer.validate() adds a slugged version of the artist attribute to the data
        """
        serializer = SoloSerializer()
        data = serializer.validate({'artist': 'Ray Brown'})

        self.assertEqual(data, {
            'artist': 'Ray Brown',
            'slug': 'ray-brown'
        })
