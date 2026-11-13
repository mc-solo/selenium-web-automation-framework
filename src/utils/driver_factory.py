"""Create and tear down the WebDriver.

One place owns browser setup, so every test gets the same clean,
headless Chrome session and no test has to know how the driver
was built. webdriver-manager downloads the matching ChromeDriver,
so there is nothing to install by hand.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.utils import config_loader


def create_driver():
    options = Options()
    if config_loader.getboolean("browser", "headless", fallback=True):
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(
        "--window-size={},{}".format(
            config_loader.getint("browser", "window_width", fallback=1920),
            config_loader.getint("browser", "window_height", fallback=1080),
        )
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    driver.set_page_load_timeout(
        config_loader.getint("browser", "page_load_timeout", fallback=30)
    )
    return driver
