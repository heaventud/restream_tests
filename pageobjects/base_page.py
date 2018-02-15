# coding=utf-8
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os.path
import sys


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def goto(self, url):
        url = self.base_url + url
        self.driver.get(url)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
