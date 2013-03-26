from unittest import TestCase
import asserts
from page.page import Page

class GoogleSearch(Page):
    @property
    def search_field(self):
        pass


class SearchTest(TestCase):
    def setup(self):
        pass

    def test_search(self):
        page = GoogleSearch(context)
        print(page.context)
        asserts.equal('3', 3)

    def tear_down(self):
        pass
