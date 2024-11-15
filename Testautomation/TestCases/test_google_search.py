import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load environment variables
load_dotenv()

# Use the ChromeDriver path from .env
service = Service(os.getenv("CHROME_DRIVER_PATH"))
driver = webdriver.Chrome(service=service)

print("Opened Masterschool website")

# Open the Masterschool website
driver.get("https://masterschool.com")
time.sleep(3)  # Wait for page to load

# Check for and accept cookies if the popup appears
try:
    accept_cookies_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Verstanden']"))
    )
    accept_cookies_button.click()
    print("Accepted cookies")
except:
    print("No cookie consent popup detected, proceeding without clicking")

# Try to find and click the "Programme" link
try:
    # Option 1: Use link text if it is unique
    programme_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Programme"))
    )
    programme_link.click()
    print("Clicked 'Programme' link using Link Text")
except:
    print("Could not find 'Programme' link with Link Text, trying with XPath")

    # Option 2: Use XPath if the link text method fails
    try:
        programme_link_xpath = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/domains/data-analytics-14-months')]"))
        )
        programme_link_xpath.click()
        print("Clicked 'Programme' link using XPath")
    except Exception as e:
        print(f"Could not click 'Programme' link using XPath: {e}")

# After clicking on the 'Programme' link, wait for the program list to appear
try:
    program_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "menu-item"))
    )
    print("Found the list of programs")

    # Loop through the programs and print their names
    for program in program_elements:
        print("Program:", program.text)

except Exception as e:
    print(f"Could not locate program list: {e}")
finally:
    # Close the browser
    driver.quit()
    print("Browser closed")
