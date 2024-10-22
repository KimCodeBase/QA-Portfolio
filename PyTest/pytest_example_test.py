#pytest pytest_example_test.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome() 
    driver.get("https://www.google.com")  
    yield driver
    driver.quit() 

def test_google_search(setup):
    driver = setup

    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )

    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", search_bar)

    try:
        search_bar.send_keys("ISTQB")
    except Exception as e:
        print(f"Failed to send keys directly, using JavaScript: {e}")
        driver.execute_script("arguments[0].value='ISTQB';", search_bar)

    search_form = driver.find_element(By.XPATH, "//form[@role='search']")
    
    driver.execute_script("arguments[0].submit();", search_form)

    WebDriverWait(driver, 10).until(EC.title_contains("ISTQB"))
    
    assert "ISTQB" in driver.title
