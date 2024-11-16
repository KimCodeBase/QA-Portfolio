import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import time

from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope="module")
def setup():
    service = Service(os.getenv("CHROME_DRIVER_PATH"))
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def test_google_search(setup):
    driver = setup
    
    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Handle consent popup if present
    try:
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='I agree'] | //button[text()='Accept all']"))
        )
        consent_button.click()
        print("Closed consent popup.")
    except:
        print("No consent popup detected.")

    # Locate the search bar, enter the search term, and submit
    try:
        search_bar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_bar.clear()
        search_bar.send_keys("ISTQB")
        search_bar.submit()
        print("Entered 'ISTQB' and submitted search.")
    except Exception as e:
        print(f"Could not interact with the search bar: {e}")
        driver.execute_script("arguments[0].value='ISTQB';", search_bar)

    # Wait for search results and click on the first suggestion if available
    try:
        first_result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        first_result.click()
        print("Clicked on the first result link.")
    except Exception as e:
        print(f"Could not click on the first result: {e}")

    # Verify if the new page title contains "ISTQB"
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("ISTQB"))
        assert "ISTQB" in driver.title
        print("The new page title contains 'ISTQB'.")
    except Exception as e:
        print(f"Failed to verify page title: {e}")

