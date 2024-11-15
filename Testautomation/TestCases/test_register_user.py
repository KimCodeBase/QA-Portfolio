import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables
load_dotenv()

# Initialize WebDriver
service = webdriver.chrome.service.Service(os.getenv("CHROME_DRIVER_PATH"))
driver = webdriver.Chrome(service=service)
print("Browser launched")

# Step 1-2: Navigate to URL
driver.get("http://automationexercise.com")
print("Navigated to automationexercise.com")

# Function to forcibly remove consent banner using JavaScript with retry
def remove_consent_banner(driver):
    for _ in range(3):  
        try:
            driver.execute_script("""
                var banner = document.querySelector('.fc-consent-root');
                if (banner) {
                    banner.remove();
                }
            """)
            print("Consent banner forcibly removed.")
            time.sleep(1)  
        except Exception as e:
            print(f"Error removing consent banner: {e}")

# Function to generate a unique email address for each run
def generate_unique_email():
    random_number = random.randint(1000, 9999)
    return f"kimberly_test_{random_number}@example.com"

# Step 3: Verify that home page is visible
assert "Automation Exercise" in driver.title
print("Home page is visible successfully.")

# Initial consent banner removal
remove_consent_banner(driver)

# Step 4: Click on 'Signup / Login' using JavaScript
try:
    signup_login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))
    )
    driver.execute_script("arguments[0].click();", signup_login_button)
    print("Clicked on 'Signup / Login' button using JavaScript")
except Exception as e:
    print(f"Error clicking 'Signup / Login' button: {e}")

# Step 5: Verify 'New User Signup!' is visible
try:
    new_user_signup = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'New User Signup!')]"))
    )
    print("'New User Signup!' is visible.")
except Exception as e:
    print(f"Error verifying 'New User Signup!' visibility: {e}")

# Step 6: Enter name and unique email address for signup
try:
    name_input = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    email_input = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")

    unique_email = generate_unique_email()
    driver.execute_script("arguments[0].value = 'Kimberly Test';", name_input)
    driver.execute_script(f"arguments[0].value = '{unique_email}';", email_input)
    print(f"Entered name and unique email address ({unique_email}) for New User Signup.")
except Exception as e:
    print(f"Error entering name or email: {e}")

# Step 7: Click 'Signup' button using JavaScript
try:
    signup_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Signup')]")
    driver.execute_script("arguments[0].click();", signup_button)
    print("Clicked 'Signup' button.")
except Exception as e:
    print(f"Error clicking 'Signup' button: {e}")

# Step 8: Remove consent banner if it reappears
remove_consent_banner(driver)

# Step 9: Fill account information
try:
    driver.execute_script("document.getElementById('id_gender1').click();")
    driver.execute_script("document.getElementsByName('password')[0].value = 'Test@123';")
    driver.execute_script("document.getElementsByName('days')[0].value = '10';")
    driver.execute_script("document.getElementsByName('months')[0].value = 'May';")
    driver.execute_script("document.getElementsByName('years')[0].value = '1990';")
    print("Filled account information.")
except Exception as e:
    print(f"Error filling account information: {e}")

# Step 10: Select checkboxes and fill personal details
try:
    driver.execute_script("document.getElementById('newsletter').click();")
    driver.execute_script("document.getElementById('optin').click();")
    driver.execute_script("document.getElementsByName('first_name')[0].value = 'Kimberly';")
    driver.execute_script("document.getElementsByName('last_name')[0].value = 'Ordonez';")
    driver.execute_script("document.getElementsByName('company')[0].value = 'TechCo';")
    driver.execute_script("document.getElementsByName('address1')[0].value = '123 Tech Street';")
    driver.execute_script("document.getElementsByName('address2')[0].value = 'Suite 100';")
    driver.execute_script("document.getElementsByName('country')[0].value = 'United States';")
    driver.execute_script("document.getElementsByName('state')[0].value = 'California';")
    driver.execute_script("document.getElementsByName('city')[0].value = 'TechCity';")
    driver.execute_script("document.getElementsByName('zipcode')[0].value = '90001';")
    driver.execute_script("document.getElementsByName('mobile_number')[0].value = '+1234567890';")
    print("Filled personal details.")
except Exception as e:
    print(f"Error filling personal details: {e}")

# Step 11: Click 'Create Account' button with retry mechanism
def click_create_account_button():
    for attempt in range(3): 
        try:
            remove_consent_banner(driver) 
            create_account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default"))
            )
            driver.execute_script("arguments[0].click();", create_account_button)
            print("Clicked 'Create Account' button.")
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} - Error clicking 'Create Account' button: {e}")
            time.sleep(2)  
    return False

if not click_create_account_button():
    print("Failed to click 'Create Account' button after multiple attempts.")

# Step 12: Verify 'ACCOUNT CREATED!' is visible
try:
    account_created = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Account Created!')]"))
    )
    print("'ACCOUNT CREATED!' is visible.")
except Exception as e:
    print(f"Error verifying 'ACCOUNT CREATED!': {e}")

# Step 13: Click 'Continue' button
try:
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Continue"))
    )
    driver.execute_script("arguments[0].click();", continue_button)
    print("Clicked 'Continue' button.")
except Exception as e:
    print(f"Error clicking 'Continue' button: {e}")

# Step 14: Verify 'Logged in as Kimberly Test' is visible
try:
    logged_in_as = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as Kimberly Test')]"))
    )
    print("'Logged in as Kimberly Test' is visible.")
except Exception as e:
    print(f"Error verifying 'Logged in as Kimberly Test': {e}")

# Step 15: Click 'Delete Account' button with retry mechanism
def click_delete_account_button():
    for attempt in range(3):  
        try:
            remove_consent_banner(driver) 
            delete_account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account"))
            )
            driver.execute_script("arguments[0].click();", delete_account_button)
            print("Clicked 'Delete Account' button.")
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} - Error clicking 'Delete Account' button: {e}")
            time.sleep(2) 
    return False

if not click_delete_account_button():
    print("Failed to click 'Delete Account' button after multiple attempts.")

# Step 16: Verify 'ACCOUNT DELETED!' and click 'Continue'
try:
    account_deleted = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Account Deleted!')]"))
    )
    print("'ACCOUNT DELETED!' is visible.")
    driver.find_element(By.LINK_TEXT, "Continue").click()
    print("Clicked 'Continue' button after account deletion.")
except Exception as e:
    print(f"Error verifying 'ACCOUNT DELETED!': {e}")

# Finalize
driver.quit()
print("Test completed, browser closed.")

