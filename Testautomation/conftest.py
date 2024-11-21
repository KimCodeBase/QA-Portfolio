import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def setup():
    """Fixture for WebDriver setup and teardown."""
    service = Service(os.getenv("CHROME_DRIVER_PATH"))
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()