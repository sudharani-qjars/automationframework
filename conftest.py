import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from utilities.data_reader import TestDataReader
from utilities.config_reader import ConfigReader
import utilities.screenshot_utils as screenshot_utils
from utilities.http_client import APIClient

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.signup_page import SignUpPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = screenshot_utils.capture_screenshot(driver, item.name)

            # if hasattr(report, "extra"):
            #     report.extra.append(pytest_html.extras.png(screenshot_path))


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
    return {
        "env": os.getenv("TEST_ENV_NAME"),
        "browser": os.getenv("BROWSER", "chrome")
    }


@pytest.fixture(scope="session")
def driver(load_env, config_data_reader):
    browser_name = load_env.get("browser", "chrome").lower()
    with sync_playwright() as p:
        browser_map = {
            "chrome": p.chromium,
            "chromium": p.chromium,
            "edge": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit,
        }
        browser_type = browser_map.get(browser_name, p.chromium)
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.set_default_timeout(15000)
        page.goto(config_data_reader.get("url"))
        yield page
        browser.close()


@pytest.fixture(scope="session")
def page(driver):
    return driver


@pytest.fixture(scope="session")
def test_data_reader(load_env):
    file_path = os.path.join(os.path.dirname(__file__), "testdata")
    file_name = "data.json"
    reader = TestDataReader(os.path.join(file_path, file_name), load_env.get("env"))
    return reader.load_data()


@pytest.fixture(scope="session")
def config_data_reader(load_env):
    file_path = os.path.join(os.path.dirname(__file__), "config")
    file_name = "config.json"
    reader = ConfigReader(os.path.join(file_path, file_name), load_env.get("env"))
    return reader.load_data()


@pytest.fixture(scope="session")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="session")
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope="session")
def signup_page(driver):
    return SignUpPage(driver)


@pytest.fixture(scope="session")
def api_executor(config_data_reader):
    return APIClient(config_data_reader.get("url"))