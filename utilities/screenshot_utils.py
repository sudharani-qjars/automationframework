import os
from datetime import datetime


def capture_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
    driver.screenshot(path=path, full_page=True)
    return path