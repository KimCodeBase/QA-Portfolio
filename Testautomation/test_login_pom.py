import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://academy.masterschool.com/login")
    yield driver
    driver.quit()

def test_successful_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter valid credentials
    login_page.enter_username("valid_user")
    login_page.enter_password("valid_password")
    login_page.click_login()

    # Wait for login success and verify
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
    )
    assert driver.find_element(By.CLASS_NAME, "dashboard").is_displayed(), "Dashboard not displayed"

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Enter invalid credentials
    login_page.enter_username("invalid_user")
    login_page.enter_password("invalid_password")
    login_page.click_login()

    # Wait for error message and verify
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
    )
    assert driver.find_element(By.CLASS_NAME, "error-message").is_displayed(), "Error message not displayed"
