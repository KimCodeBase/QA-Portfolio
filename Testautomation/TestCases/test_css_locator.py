import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load environment variables
load_dotenv()

# Use the ChromeDriver path from .env
service = Service(os.getenv("CHROME_DRIVER_PATH"))
driver = webdriver.Chrome(service=service)

# Open the local HTML file
driver.get(os.getenv("HTML_FILE_PATH"))
print("Opened local HTML file")

# Locate the input field using CSS selector and enter text
try:
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#inputField"))
    )
    input_field.send_keys("Test with CSS Locator")
    print("Entered text in the input field")
except Exception as e:
    print(f"Could not interact with the input field: {e}")

# Locate the submit button using CSS selector and click it
try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton"))
    )
    submit_button.click()
    print("Clicked the submit button")
except Exception as e:
    print(f"Could not interact with the submit button: {e}")

# Wait for the output text and print it
WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "output"), "You entered:")
)
output_text = driver.find_element(By.ID, "output").text
print("Output:", output_text)

# Pause for 5 seconds to observe
time.sleep(5)

# Close the browser
driver.quit()
print("Browser closed")
