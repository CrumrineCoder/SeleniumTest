import pytest
import os

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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)