from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    """ This class contains all code and settings of selenium driver with chrome browser settings. """

    WINDOW_WIDTH = 1400
    """ int: Browser window width. """

    WINDOW_HEIGHT = 600
    """ int: Browser window height. """

    def __init__(self, headless=False):
        self.headless = headless
        self.driver = webdriver.Chrome(chrome_options=self.options)

    @property
    def options(self):
        """ Custom options for chrome browser. """
        opt = Options()
        self.headless and opt.add_argument('--headless')
        opt.add_argument(f'window-size={self.WINDOW_WIDTH},{self.WINDOW_HEIGHT}')
        opt.add_argument("--disable-gpu")
        opt.add_argument("--no-sandbox")
        opt.add_argument('--disable-dev-shm-usage')
        return opt

    def __getattr__(self, item):
        return self.driver.__getattribute__(item)
