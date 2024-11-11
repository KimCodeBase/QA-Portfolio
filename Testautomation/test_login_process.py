from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter the username
username = driver.find_element(By.ID, "username")
username.send_keys("student")

# Enter the password
password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

# Click the login button
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Wait for a few seconds to verify the login
time.sleep(3)

# Print the title of the page after login
print(driver.title)

# Close the browser
driver.quit()
