import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")
    yield driver
    driver.quit()

def test_wikipedia_search(setup):
    driver = setup

    # Locate search bar and enter "Selenium WebDriver"
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Selenium WebDriver")

    # Submit the search
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for the search results to load and verify the presence of "Selenium WebDriver" text
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Selenium (software)')]"))
    )

    assert "Selenium (software)" in driver.page_source, "Text 'Selenium WebDriver' not found on page"
