## Test Execution Report - Automating Google Search Using Selenium and PyTest

**Test Objective**:  
The objective of this task was to automate the Google search process using Selenium WebDriver with Python, verify that the search bar on Google's homepage is interactable, and simulate a search action. The test aimed to check if the search term "ISTQB" could be entered and the results page could be accessed.

**Test Steps**:  
1. **Installed PyTest**:  
   Installed PyTest using the command:  
   pip install pytest
   

2. **Installed Selenium and WebDriver**:  
   Installed Selenium and Chrome WebDriver for the automation 
   pip install selenium
   install chromedriver or brew install chromedriver

3. **Test Script Development**:  
   - Created a PyTest script (`pytest_example_test.py`) that uses Selenium WebDriver to launch Chrome and navigate to Google.
   - Located the search bar using its element attributes.
   - Simulated entering "ISTQB" into the search bar and triggered the search using JavaScript when direct interaction was not possible.

4. **Element Handling**:  
   - Ensured that the search bar was visible, enabled, and interactable.
   - Used JavaScript to interact with the element when the normal send_keys method encountered issues.

5. **Executed the Test**:  
   Ran the PyTest test case using:  
   pytest pytest_example_test.py
   
**Test Results**:  
- **Test Passed**: The test successfully simulated a Google search for "ISTQB," interacted with the search bar, and opened the results page as expected.
- **Output**: The test script ran without any errors, and the expected search was executed.

**Key Challenges and Solutions**:  
- Initially encountered the `ElementNotInteractableException` due to Google's dynamic page and the use of a shadow DOM.
- The issue was resolved by using JavaScript to interact with the element when direct interaction was not possible.

**Conclusion**:  
This test case demonstrates the ability to automate basic web interactions using Selenium WebDriver and PyTest. By handling potential interaction issues with elements using fallback methods like JavaScript, we successfully achieved the test's objective.
