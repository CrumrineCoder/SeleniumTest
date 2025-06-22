from datetime import datetime
import json

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename

def load_test_data(filename):
    with open(f'configuration/{filename}', 'r') as f:
        return json.load(f)