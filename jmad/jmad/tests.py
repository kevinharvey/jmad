from django.test import LiveServerTestCase

from selenium import webdriver

from solos.models import Solo


class StudentTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

        self.solo1 = Solo.objects.create(
            instrument='saxophone',
            artist='Coltrane',
            track='My Favorite Things',
            album='My Favorite Things'
        )
        self.solo2 = Solo.objects.create(instrument='saxophone', artist='Adderley', track='All Blues',
                                         album='Kind of Blue', start_time='2:06', end_time='4:01')
        self.solo3 = Solo.objects.create(instrument='saxophone', artist='Adderley', track='Waltz for Debby',
                                         album='Know What I Mean?')

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
        instrument_input = self.browser.find_element_by_css_selector('input#jmad-instrument-input')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-instrument-input"]'))
        self.assertEqual(instrument_input.get_attribute('placeholder'), 'i.e. trumpet')

        artist_input = self.browser.find_element_by_css_selector('input#jmad-artist-input')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-artist-input"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Davis')

        # He types in the name of his instrument and submits it.
        instrument_input.send_keys('saxophone')
        instrument_input.submit()

        # He sees too many search results...
        search_results = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertGreater(len(search_results), 2)

        # ... so he adds a particular artist to his search query and gets a more manageable list.
        second_artist_input = self.browser.find_element_by_css_selector('input#jmad-artist-input')
        second_artist_input.send_keys('Adderley')
        second_artist_input.submit()

        second_search_results = self.browser.find_elements_by_css_selector('.jmad-search-result a')
        self.assertEqual(len(second_search_results), 2)

        # He clicks on one of the search results.
        second_search_results[0].click()

        # On the solo page...
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + '/recordings/kind-of-blue/all-blues/cannonball-adderley/')

        # he sees the artist...
        self.assertEqual(
            self.browser.find_element_by_css_selector('#jmad-artist').text,
            'Adderley'
        )
        # track title (with a count of solos)...
        self.assertEqual(
            self.browser.find_element_by_css_selector('#jmad-track').text,
            'All Blues [2 solos]'
        )

        # and album title (with track count) for this solo.
        self.assertEqual(
            self.browser.find_element_by_css_selector('#jmad-album').text,
            'Kind of Blue [3 tracks]'
        )

        # He also sees the start time and end time of the solo.
        self.assertEqual(
            self.browser.find_element_by_css_selector('#jmad-start-time').text,
            '2:06'
        )
        self.assertEqual(
            self.browser.find_element_by_css_selector('#jmad-end-time').text,
            '4:01'
        )

        # Steve is interested in seeing the other solos on the track, so he clicks it's title
        self.browser.find_element_by_css_selector('#jmad-track')


