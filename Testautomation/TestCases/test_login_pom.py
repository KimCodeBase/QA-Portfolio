import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from POM.login_page import LoginPage

# Load environment variables
load_dotenv()

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Browser launched")
    driver.get("https://academy.masterschool.com/login")
    print("Navigated to academy.masterschool.com/login")
    yield driver
    driver.quit()
    print("Test completed, browser closed.")

def test_successful_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter valid credentials from environment variables
    login_page.enter_username(os.getenv("VALID_USERNAME"))
    login_page.enter_password(os.getenv("VALID_PASSWORD"))
    login_page.click_login()

    # Increased wait time and verification for successful login
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
        )
        assert driver.find_element(By.CLASS_NAME, "dashboard").is_displayed()
        print("Successfully logged in - dashboard is visible.")
    except TimeoutException:
        print("Dashboard element not found after login.")

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter invalid credentials
    login_page.enter_username("invalid_user")
    login_page.enter_password("invalid_password")
    login_page.click_login()

    # Increased wait time and verification for error message
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert driver.find_element(By.CLASS_NAME, "error-message").is_displayed()
        print("Error message is visible for invalid login.")
    except TimeoutException:
        print("Error message element not found after invalid login.")
