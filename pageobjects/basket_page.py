from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException, NoSuchElementException)
from base_page import BasePage


class BasketPage(BasePage):
    """
    Class represents Basket page
    """

    def __init__(self, driver):
        self.driver = driver
        super(BasketPage, self).__init__(self.driver)
        try:
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//h3[text()='Your Basket']")))
        except TimeoutException:
            raise NoSuchElementException("This is not Basket page")

    def get_products_in_basket(self):
        products = self.driver.find_elements(By.XPATH, "//table/tbody/tr[@data-ng-repeat='product in products']")
        basket = list()
        for prod in products:
            basket.append(Product(prod))
        return basket


class Product(object):
    def __init__(self, tag):
        self.el = tag

    @property
    def name(self):
        return self.el.find_element_by_xpath("./td[1]").text

    @property
    def description(self):
        return self.el.find_element_by_xpath("./td[2]").text

    @property
    def price(self):
        return self.el.find_element_by_xpath("./td[3]").text
