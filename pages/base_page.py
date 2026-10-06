"""
base_page.py

Contains common Playwright operations used across all pages.
"""

from typing import Optional, Union, Iterable
from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str, timeout: Optional[float] = None) -> None:
        """Navigate to a URL."""
        self.page.goto(url, timeout=timeout)

    def click(self, locator: str, timeout: Optional[float] = None, force: bool = False) -> None:
        """Click an element using locator API."""
        self.page.locator(locator).click(timeout=timeout, force=force)

    def enter_text(self, locator: str, text: str, timeout: Optional[float] = None) -> None:
        """Enter text into a field (uses fill which clears existing value)."""
        self.page.locator(locator).fill(text, timeout=timeout)

    def get_text(self, locator: str, timeout: Optional[float] = None) -> str:
        """Get visible text from an element."""
        return self.page.locator(locator).inner_text(timeout=timeout)

    def is_visible(self, locator: str, timeout: Optional[float] = None) -> bool:
        """Check if element is visible."""
        return self.page.locator(locator).is_visible(timeout=timeout)

    def wait_for_element(self, locator: str, state: str = "visible", timeout: Optional[float] = None) -> None:
        """Wait for element to reach a given state ('visible','hidden','attached','detached')."""
        self.page.locator(locator).wait_for(state=state, timeout=timeout)

    def get_title(self) -> str:
        """Get page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Get current URL."""
        return self.page.url

    def take_screenshot(self, file_name: str, full_page: bool = False, timeout: Optional[float] = None) -> None:
        """Capture screenshot."""
        self.page.screenshot(path=file_name, full_page=full_page, timeout=timeout)

    def press_key(self, locator: str, key: str, timeout: Optional[float] = None) -> None:
        """Press keyboard key on an element."""
        self.page.locator(locator).press(key, timeout=timeout)

    def select_dropdown(self, locator, value, timeout: Optional[float] = None) -> None:
        """Select dropdown value. Accepts a single value, dict or list of values."""
        loc = self.page.locator(locator)
        loc.select_option(str(value), timeout=timeout)

    def check_checkbox(self, locator: str, timeout: Optional[float] = None) -> None:
        """Check checkbox."""
        self.page.locator(locator).check(timeout=timeout)

    def uncheck_checkbox(self, locator: str, timeout: Optional[float] = None) -> None:
        """Uncheck checkbox."""
        self.page.locator(locator).uncheck(timeout=timeout)

    def hover(self, locator: str, timeout: Optional[float] = None) -> None:
        """Hover over an element."""
        self.page.locator(locator).hover(timeout=timeout)

    def double_click(self, locator: str, timeout: Optional[float] = None) -> None:
        """Double click on an element."""
        self.page.locator(locator).dblclick(timeout=timeout)

    def scroll_into_view(self, locator: str, timeout: Optional[float] = None) -> None:
        """Scroll element into view."""
        self.page.locator(locator).scroll_into_view_if_needed(timeout=timeout)

    def upload_file(self, locator: str, file_path: Union[str, Iterable[str]], timeout: Optional[float] = None) -> None:
        """Upload file. Accepts single path or list of paths."""
        loc = self.page.locator(locator)
        if isinstance(file_path, (list, tuple)):
            loc.set_input_files(list(file_path), timeout=timeout)
        else:
            loc.set_input_files(str(file_path), timeout=timeout)
