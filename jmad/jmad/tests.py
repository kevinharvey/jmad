from django.test import LiveServerTestCase

from selenium import webdriver

from solos.models import Solo


class StudentTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

        self.solo1 = Solo.objects.create(instrument='saxophone', artist='John Coltrane', track='My Favorite Things')
        self.solo2 = Solo.objects.create(instrument='saxophone', artist='Cannonball Adderley', track='All Blues')
        self.solo3 = Solo.objects.create(instrument='saxophone', artist='Cannonball Adderley', track='Waltz for Debby')

    def tearDown(self):
        self.browser.quit()

    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """
        # Steve is a jazz student who would like to find more examples of solos so he can improve his own improvisation.
        # He visits the home page of JMAD.
        home_page = self.browser.get(self.live_server_url + '/')

        # He knows he's in the right place because he can see the name of the site in the heading.
        brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        self.assertEqual('JMAD', brand_element.text)

        # He sees the inputs of the search form, including labels and placeholders.
        instrument_input = self.browser.find_element_by_css_selector('input#jmad-instrument')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-instrument"]'))
        self.assertEqual(instrument_input.get_attribute('placeholder'), 'i.e. trumpet')

        artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-artist"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Davis')

        # He types in the name of his instrument and submits it.
        instrument_input.send_keys('saxophone')
        self.browser.find_element_by_css_selector('form button').click()

        # He sees too many search results...
        search_results = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertGreater(len(search_results), 2)

        # ...so he adds an artist to his search query and gets a more manageable list.
        second_artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
        second_artist_input.send_keys('Cannonball Adderley')
        self.browser.find_element_by_css_selector('form button').click()

        second_search_results = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertEqual(len(second_search_results), 2)

        # He clicks on a search result.
        second_search_results[0].click()

        # The solo page has the title, artist and album for this particular solo.
        self.assertEqual(self.browser.current_url, '{}/solos/2/'.format(self.live_server_url))

        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-artist').text, 'Adderley')
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-track').text, 'All Blues')
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-album').text, 'Kind of Blue')

        # He also sees the start time and end time of the solo.
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-start-time').text, '2:06')
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-end-time').text, '4:01')
