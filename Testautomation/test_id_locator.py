import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load environment variables
load_dotenv()

# Use the ChromeDriver path from .env
service = webdriver.chrome.service.Service(os.getenv("CHROME_DRIVER_PATH"))
driver = webdriver.Chrome(service=service)

# Open the local HTML file using the path from .env
driver.get(os.getenv("LOCAL_HTML_PATH"))
print("Opened local HTML file")

# Wait for the page to load
time.sleep(2)

# Locate input field using ID and type some text
input_field = driver.find_element(By.ID, "inputField")
input_field.send_keys("Test")

# Locate and click the submit button 
try:
    submit_button = driver.find_element(By.ID, "submitButton")
    submit_button.click()
    print("Clicked the submit button")
except:
    print("Submit button not found or clickable")

# Wait for 2 seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()
print("Browser closed")
