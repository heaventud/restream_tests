import ConfigParser
import os.path
from selenium import webdriver
import config


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = os.getcwd() + '/binaries/chromedriver.exe'
    # ie_driver_path = dir + '/binaries/IEDriverServer.exe'

    def open_browser(self):
        browser = config.BROWSER
        url = config.BASE_URL

        if browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-extensions")
            driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=self.chrome_driver_path)
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(2)
        return driver

    def quit_browser(self):
        self.driver.quit()
