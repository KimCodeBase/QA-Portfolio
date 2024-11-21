import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.wikipedia_search_page import WikipediaSearchPage
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")
    yield driver
    driver.quit()

def test_wikipedia_search_pom(setup):
    driver = setup
    search_page = WikipediaSearchPage(driver)

    # Use the page object model to interact with the search page
    search_page.enter_search_term("Selenium WebDriver")
    search_page.click_search()

    # Wait for the search results to load and verify the presence of "Selenium WebDriver" text
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Selenium (software)')]"))
    )

    assert "Selenium (software)" in driver.page_source, "Text 'Selenium WebDriver' not found on page"