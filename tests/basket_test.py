import sys
import os
import time
sys.path.append(os.getcwd())
import unittest
import pytest
import re
from pageobjects.main_page import MainPage
from pageobjects.basket_page import BasketPage

query = 'OWASP'


@pytest.fixture(scope='class')
def classSetup(request, web_driver):
        driver = web_driver
        main_page = MainPage(driver)
        main_page.do_search(query)
        sort_by_price = main_page.get_sort_rows_by_price()[::-1]
        for_buy = sort_by_price[:2]
        request.cls.for_buy = dict([(s.product_name, s.product_price) for s in for_buy])
        for row in for_buy:
            row.add_to_basket()
            time.sleep(0.5)
        main_page.go_to_basket()
        request.cls.basket_page = BasketPage(driver)


@pytest.mark.usefixtures("classSetup")
class BasketTest(unittest.TestCase):
    """
    """
    def test_adding_to_basket(self):
        prods = self.basket_page.get_products_in_basket()
        in_basket = dict([(s.name, s.price) for s in prods])
        self.assertEqual(in_basket, self.for_buy,
                         "Expected products:\r\n" + "\r\n".join(self.for_buy) +
                         "\r\nBut in basket:\r\n" + "\r\n".join(in_basket))
