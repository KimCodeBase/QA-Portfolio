from selenium.webdriver.common.by import By

class WikipediaSearchPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    search_input = (By.ID, "searchInput")
    search_button = (By.XPATH, "//button[@type='submit']")

    # Methods to interact with elements
    def enter_search_term(self, term):
        self.driver.find_element(*self.search_input).send_keys(term)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()
