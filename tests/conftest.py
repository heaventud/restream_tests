import pytest
from selenium import webdriver
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
import config



"""
@pytest.yield_fixture(scope="session", autouse=True)
def oneTimeSetUp():
    print("Running one time setUp")
    browser = BrowserEngine()

    driver = browser.open_browser()

    yield driver
    driver.quit()
    print("Running one time tearDown")
"""


@pytest.fixture(scope='session', autouse=True)
def web_driver(request):
    b = BrowserEngine()
    driver = b.open_browser()
    request.addfinalizer(lambda *args: driver.quit())
    return driver


@pytest.fixture(scope="session", autouse=True)
def loginBeforeTests(web_driver):
    driver = web_driver
    driver.find_element_by_xpath("//a[@href='#/login']").click()
    # driver.get(config.BASE_URL + '/#/login')
    login_page = LoginPage(driver)
    login_page.do_login(config.LOGIN, config.PASSWORD)