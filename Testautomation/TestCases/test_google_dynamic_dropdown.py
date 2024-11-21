from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Wait for the search bar to be visible
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Verify that the search bar is visible
    assert search_bar.is_displayed(), "Search bar is not visible"

    # Enter search term "ISTQB"
    search_bar.send_keys("ISTQB")

    # Wait for the dropdown to appear
    time.sleep(2)

    # Press "down arrow" to select the first result and then "Enter" to click
    search_bar.send_keys(Keys.ARROW_DOWN)
    search_bar.send_keys(Keys.ENTER)

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(
        EC.title_contains("ISTQB")
    )

    # Verify that the new page is opened (title contains "ISTQB")
    assert "ISTQB" in driver.title, "New page did not open correctly"

finally:
    # Quit the browser
    driver.quit()