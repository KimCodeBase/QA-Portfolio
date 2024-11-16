## Test Execution Report - Automating Google Search Using Selenium and PyTest

**Test Objective**:  
The objective of this task was to automate the Google search process using Selenium WebDriver with Python, verify that the search bar on Google's homepage is interactable, and simulate a search action. The test aimed to check if the search term "ISTQB" could be entered and the results page could be accessed.

**Test Steps**:  
1. Created a PyTest script (pytest_example_test.py) that:
- Used Selenium WebDriver to open Chrome and navigate to Google.
- Located the search bar and entered "ISTQB."
- Used JavaScript to interact with elements if direct methods   encountered issues.
   

2. Ran the test case with pytest pytest_example_test.py.
 **Test Results:**
- Test Passed: The script successfully simulated a Google search for "ISTQB" and navigated to the results page.
- Output: The test ran without errors, executing the expected actions.

**Conclusion**:  
This test case demonstrates the ability to automate basic web interactions using Selenium WebDriver and PyTest. By handling potential interaction issues with elements using fallback methods like JavaScript, I successfully achieved the test's objective.
