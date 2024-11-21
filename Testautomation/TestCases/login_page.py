from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Updated Locators (verify these in the browser if necessary)
    username_input = (By.NAME, "username")  # Confirm if correct
    password_input = (By.NAME, "password")  # Confirm if correct
    login_button = (By.XPATH, "//button[@type='submit']")  # Confirm if correct

    # Methods to interact with elements
    def enter_username(self, username):
        try:
            self.driver.find_element(*self.username_input).send_keys(username)
        except NoSuchElementException:
            print("Username input not found.")

    def enter_password(self, password):
        try:
            self.driver.find_element(*self.password_input).send_keys(password)
        except NoSuchElementException:
            print("Password input not found.")

    def click_login(self):
        try:
            self.driver.find_element(*self.login_button).click()
        except NoSuchElementException:
            print("Login button not found.")
