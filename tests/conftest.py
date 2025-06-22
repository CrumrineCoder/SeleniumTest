import pytest
from utils.driver_factory import DriverFactory
from configuration.settings import BASE_URL

@pytest.fixture(scope="function")
def driver():
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def test_data():
    import json
    with open('configuration/test_data.json', 'r') as f:
        return json.load(f)