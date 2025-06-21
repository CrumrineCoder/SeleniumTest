import os

BASE_URL = os.getenv('BASE_URL', 'https://www.selenium.dev/selenium/web/web-form.html')
BROWSER = os.getenv('BROWSER', 'firefox')
HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
TIMEOUT = int(os.getenv('TIMEOUT', '10'))

TEST_USERS = {

}