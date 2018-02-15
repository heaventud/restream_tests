import sys
import os
sys.path.append(os.getcwd())
import config
import unittest
import pytest
import re
from pageobjects.main_page import MainPage

query = 'OWASP'


@pytest.fixture(scope='class')
def classSetup(request, web_driver):
        driver = web_driver
        main_page = MainPage(driver)
        main_page.do_search(query)
        request.cls.results = main_page.get_table_rows()


@pytest.mark.usefixtures("classSetup")
class SearchTest(unittest.TestCase):

    def test_results_attributes(self):
        """
        check that all results contains OWASP
        """
        names = [s.product_name for s in self.results if query in s.product_name]
        self.assertEqual(len(names), len(self.results),
                         "Some results don't contain substring " + query + "in name \r\n" )

    def test_results_descriptions(self):
        descriptions = [s.product_description for s in self.results if s.product_description != ""]
        self.assertEqual(len(descriptions), len(self.results),
                         "Some results don't contain description")

    def test_results_images(self):
        images = [s.product_image for s in self.results if
                  re.search(config.BASE_URL + "/public/images/products/.*(jpg|png)",
                            s.product_image)]
        self.assertEqual(len(images), len(self.results),
                         "Some results don't contain images\r\n" + "\r\n".join(images))

    def test_results_prices(self):
        prices = [s.product_price for s in self.results if re.search("\d+\.\d+", s.product_price)]
        self.assertEqual(len(prices), len(self.results),
                         "Some results don't contain prices\r\n" + "\r\n".join(prices))



