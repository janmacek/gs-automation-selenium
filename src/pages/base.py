import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.driver import Driver
from src.settings import settings


class BasePage:
    """ Base web page that opens window with desired URL and it has methods to work with elements using xpath. """

    URL = None
    """ str: If set, after initialization of page object, browser is redirected to this URL. """

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = Driver()
        if self.URL:
            self.driver.driver.get(self.URL)
        self.logger = logging.getLogger(str(settings.PROJECT_DIR))
        self.logger.info(f'Class \'{self.__class__.__name__}\' successfully initialized.')

    def close(self):
        self.driver.close()

    def get_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def get_elements_by_xpath(self, xpath):
        return self.driver.driver.find_elements_by_xpath(xpath)

    def click_element_by_xpath(self, xpath, scroll_to=False):
        if scroll_to:
            self.scroll_to_element_by_xpath(xpath)
            time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.get_element_by_xpath(xpath))
        time.sleep(0.3)

    def scroll_to_element_by_xpath(self, xpath):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({behavior: "smooth"});', self.get_element_by_xpath(xpath)
        )

    def set_value_by_xpath(self, xpath, value):
        elem = self.get_element_by_xpath(xpath)
        elem.clear()
        elem.send_keys(value)
        time.sleep(0.3)

    @staticmethod
    def get_child_by_xpath(elem, xpath):
        return WebDriverWait(elem, 10).until(lambda _: elem.find_element_by_xpath(xpath))

    def click_child_by_xpath(self, elem, xpath):
        self.driver.execute_script('arguments[0].click();', self.get_child_by_xpath(elem, xpath))

    def get_child_text_by_xpath(self, elem, xpath):
        return self.get_child_by_xpath(elem, xpath).text
