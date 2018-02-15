from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException, NoSuchElementException)
from base_page import BasePage


class LoginPage(BasePage):
    """
    Class represents Login page
    """

    def __init__(self, driver):
        self.driver = driver
        super(LoginPage, self).__init__(self.driver)
        try:
            self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//h3[text()='Login']")))
        except TimeoutException:
            raise NoSuchElementException("This is not Login page")

    # Methods
    def do_login(self, user, pswd):
        # self.driver.find_element_by_xpath("//a[@href='#/login']").click()
        login_form = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@name='form']")))
        email_field = login_form.find_element_by_id('userEmail')
        password_field = login_form.find_element_by_id('userPassword')
        self.enter_text(email_field, user)
        self.enter_text(password_field, pswd)
        login_form.find_element_by_id('loginButton').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#/logout']")))
