from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TextInputPage(BasePage):

    BASE_TEXTINPUT = (By.ID, 'my-text-id')

    def __init__(self, driver):
        super().__init__(driver)

    def edit_normal_input(self, input_text):
        self.enter_text(self.BASE_TEXTINPUT, input_text)

    def get_normal_input_value(self):
        return self.get_input_value(self.BASE_TEXTINPUT)