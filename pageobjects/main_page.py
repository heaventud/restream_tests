import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (TimeoutException, NoSuchElementException)
from base_page import BasePage


class MainPage(BasePage):
    """
    Class represents Main page
    """
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        #try:
        #    self.wait.until(EC.visibility_of_element_located((
        #        By.XPATH, "//h3[text()='Login']")))
        #except TimeoutException:
        #    raise NoSuchElementException("This is not Main page")

    def click_search_button(self):
        self.driver.find_element(By.ID, "searchButton").click()

    def do_search(self, query):
        """
        Perform search by query
        :param query:
        :return:
        """
        searchField = self.driver.find_element(By.XPATH, "//input[@ng-model='searchQuery']")
        searchField.clear()
        searchField.send_keys(query)
        self.click_search_button()

    def get_table_rows(self):
        rows = self.driver.find_elements(By.XPATH, "//table/tbody/tr[@class='ng-scope']")
        row_list = list()
        for row in rows:
            row_list.append(Row(row))
        return row_list

    def get_sort_rows_by_price(self):
        rows = self.get_table_rows()
        rows.sort(key=lambda x: float(x.product_price))
        return rows

    def add_product_with_index_to_basket(self, index):
        rows = self.get_table_rows()

    def go_to_basket(self):
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#/basket']")))
        el.click()


class Row(object):
    def __init__(self, tag):
        self.el = tag

    @property
    def product_image(self):
        return self.el.find_element_by_xpath("./td[1]/img").get_attribute('src')

    @property
    def product_name(self):
        return self.el.find_element_by_xpath("./td[2]").text

    @property
    def product_description(self):
        return self.el.find_element_by_xpath("./td[3]").text

    @property
    def product_price(self):
        return self.el.find_element_by_xpath("./td[4]").text

    def add_to_basket(self):
        btn = self.el.find_element_by_xpath("./td//a[contains(@ng-click, 'addToBasket')]")
        time.sleep(0.2)
        btn.click()
