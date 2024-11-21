import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException

class TestCase9(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Step 1: Launch the browser
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        print("Browser launched")

        # Step 2: Navigate to the URL 'http://automationexercise.com'
        cls.driver.get("http://automationexercise.com")
        print("Navigated to automationexercise.com")
        time.sleep(2)

        # Remove the consent banner if it appears
        cls.remove_consent_banner()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed, browser closed.")

    @classmethod
    def remove_consent_banner(cls):
        try:
            for _ in range(3):
                cls.driver.execute_script("""
                    var banner = document.querySelector('.fc-consent-root');
                    if (banner) {
                        banner.remove();
                    }
                """)
                print(f"Attempt {_ + 1}: Consent banner forcibly removed.")
                time.sleep(1)
        except Exception as e:
            print(f"Error removing consent banner: {e}")

    def test_search_product(self):
        # Step 3: Verify home page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Home')]"))
            )
            print("Home page is visible.")
        except TimeoutException:
            self.fail("Home page did not load successfully.")

        # Step 4: Click on 'Products' button
        try:
            products_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))
            )
            products_button.click()
            print("Clicked on 'Products' button.")
        except Exception as e:
            self.fail(f"Error clicking 'Products' button: {e}")

        # Step 5: Verify navigation to ALL PRODUCTS page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'All Products')]"))
            )
            print("Navigated to 'ALL PRODUCTS' page successfully.")
        except TimeoutException:
            self.fail("Navigation to 'ALL PRODUCTS' page failed.")

        # Step 6: Enter product name in search input and click search button
        try:
            # Set a product name in the search input
            self.driver.execute_script("document.getElementById('search_product').value = 'Tshirt';")
            print("Set search term in the search input.")

            # Click the search button with JavaScript
            search_button = self.driver.find_element(By.ID, "submit_search")
            self.driver.execute_script("arguments[0].click();", search_button)
            print("Clicked the search button.")
            time.sleep(2)
        except (TimeoutException, ElementClickInterceptedException, ElementNotInteractableException) as e:
            self.driver.save_screenshot('search_input_error.png')
            self.fail(f"Error entering product name or clicking search button: {e}")

        # Step 7: Verify 'SEARCHED PRODUCTS' is visible
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Searched Products')]"))
            )
            print("'SEARCHED PRODUCTS' is visible.")
        except TimeoutException as e:
            self.driver.save_screenshot('verify_search_error.png')
            self.fail(f"Error verifying 'SEARCHED PRODUCTS' visibility: {e}")

        # Step 8: Verify that all products related to search are visible
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='productinfo text-center']"))
            )
            print("All related products are visible.")
        except TimeoutException:
            self.fail("Products related to search are not visible.")

if __name__ == "__main__":
    unittest.main()