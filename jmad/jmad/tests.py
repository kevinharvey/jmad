from django.test import LiveServerTestCase

from selenium import webdriver


class StudentTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

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
        self.fail('Incomplete Test')


        # He sees the inputs of the search form, including labels and placeholders.

        # He types in the name of his instrument and submits it.

        # He sees too many search results...

        # ...so he adds an artist to his search query and gets a more manageable list.

        # He clicks on a search result.

        # The solo page has the title, artist and album for this particular solo.

        # He also sees the start time and end time of the solo.
