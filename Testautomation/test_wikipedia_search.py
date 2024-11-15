import os
import time
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Load environment variables
load_dotenv()

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get(os.getenv("WIKIPEDIA_URL", "https://www.wikipedia.org"))
    yield driver
    driver.quit()

def take_screenshot(driver, step_name):
    """Takes a screenshot with a given step name."""
    filename = f"screenshot_{step_name}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot taken: {filename}")

def test_wikipedia_search(setup):
    driver = setup

    # Locate search bar and enter "Selenium WebDriver"
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Selenium WebDriver")
    print("Entered search term in the search bar.")
    take_screenshot(driver, "after_entering_search_term")

    # Submit the search
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Clicked search button.")
    take_screenshot(driver, "after_clicking_search")

    try:
        # Check if "Selenium (software)" is listed in the search results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Selenium (software)"))
        )
        print("Found 'Selenium (software)' in the search results.")
        take_screenshot(driver, "after_search_results_load")

        # Click on the "Selenium (software)" link
        driver.find_element(By.LINK_TEXT, "Selenium (software)").click()

        # Wait for the article page to load and verify the heading
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        page_heading = driver.find_element(By.ID, "firstHeading").text
        print(f"Page heading after navigating: {page_heading}")
        take_screenshot(driver, "after_navigating_to_article")

        # Assert to check if "Selenium" is in the page heading
        assert "Selenium" in page_heading, "Expected text not found in the page heading."

        # Additional wait to allow visual confirmation
        time.sleep(5)  # Wait for 5 seconds

    except TimeoutException:
        print("Timed out waiting for the search results or article page.")
        take_screenshot(driver, "timeout_occurred")
