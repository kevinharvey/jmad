from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.six import StringIO


class CreateSuperuserTest(TestCase):

    def test_create_superuser(self):
        """
        Test that we can create a superuser by username
        """
        out = StringIO()

        call_command('jmad_create_superuser', 'bill', 'bill@example.com', stdout=out)

        self.assertIn('User \'bill\' created with default password', out.getvalue())
        user = get_user_model().objects.get(username='bill')
        self.assertTrue(user.check_password('musicianship'))

    def test_create_superuser_handles_duplicates(self):
        """
        Test that we can create a superuser by username
        """
        out = StringIO()
        get_user_model().objects.create_superuser(username='bill', email='bill@example.com', password='musicianship')

        call_command('jmad_create_superuser', 'bill', 'bill@example.com', stdout=out)

        self.assertIn('User \'bill\' already exists', out.getvalue())
