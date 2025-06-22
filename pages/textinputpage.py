from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TextInputPage(BasePage):

    BASE_TEXTINPUT = (By.ID, 'my-text-id')

    def __init__(self, driver):
        super().__init__(driver)

    def normal_is_editable(self):
        self.enter_text(self, self.BASE_TEXTINPUT, "Hi")
