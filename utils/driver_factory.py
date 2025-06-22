from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configuration.settings import HEADLESS, BROWSER

class DriverFactory:
    @staticmethod
    def get_driver():
        if BROWSER.lower() == 'chrome':
            options = Options()
            if HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            return webdriver.Chrome(options=options)
        elif BROWSER.lower() == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError(f"Browser {BROWSER} not supported")