# Test Report: Automation Exercise Account Creation and Deletion

**Objective:**
Verify that the script automates account creation, login, and deletion on the Automation Exercise website, handling consent popups and generating a unique email for each test run.

**Test Cases Executed:**

- TC-01: Open the Automation Exercise website.
Result: Website opened successfully – Pass

- TC-02: Remove the consent banner if it appears.
Result: Consent banner removed successfully using JavaScript – Pass

- TC-03: Click on the "Signup / Login" button.
Result: Button located and clicked; navigated to signup page – Pass

- TC-04: Verify "New User Signup!" is visible.
Result: "New User Signup!" message displayed – Pass

- TC-05: Enter name and unique email for signup.
Result: Name and dynamically generated email entered successfully – Pass

- TC-06: Click the "Signup" button.
Result: Button clicked; navigated to account creation form – Pass

- TC-07: Fill in account information (gender, password, birth date).
Result: Account information filled successfully – Pass

- TC-08: Select newsletter and special offers checkboxes, and fill in personal details (address, country, etc.).
Result: Personal details and checkboxes filled successfully – Pass

- TC-09: Click "Create Account" button with retry mechanism.
Result: "Create Account" button clicked successfully – Pass

- TC-10: Verify "ACCOUNT CREATED!" message.
Result: "ACCOUNT CREATED!" message displayed – Pass

- TC-11: Click "Continue" button to proceed.
Result: "Continue" button clicked; navigated to account page – Pass

- TC-12: Verify "Logged in as Kimberly Test" is visible.
Result: Logged in verification successful – Pass

- TC-13: Click "Delete Account" button with retry mechanism.
Result: "Delete Account" button clicked successfully – Pass

- TC-14: Verify "ACCOUNT DELETED!" message and click "Continue."
Result: "ACCOUNT DELETED!" message displayed; "Continue" button clicked – Pass


Test Report: Automation Exercise Account Creation and Deletion
Objective:
Verify that the script automates account creation, login, and deletion on the Automation Exercise website, handling consent popups and generating a unique email for each test run.

Environment:
macOS, Chrome Version 130.0.6723.92, Selenium WebDriver, Python.

Test Cases Executed:

TC-01: Open the Automation Exercise website.
Result: Website opened successfully – Pass

TC-02: Remove the consent banner if it appears.
Result: Consent banner removed successfully using JavaScript – Pass

TC-03: Click on the "Signup / Login" button.
Result: Button located and clicked; navigated to signup page – Pass

TC-04: Verify "New User Signup!" is visible.
Result: "New User Signup!" message displayed – Pass

TC-05: Enter name and unique email for signup.
Result: Name and dynamically generated email entered successfully – Pass

TC-06: Click the "Signup" button.
Result: Button clicked; navigated to account creation form – Pass

TC-07: Fill in account information (gender, password, birth date).
Result: Account information filled successfully – Pass

TC-08: Select newsletter and special offers checkboxes, and fill in personal details (address, country, etc.).
Result: Personal details and checkboxes filled successfully – Pass

TC-09: Click "Create Account" button with retry mechanism.
Result: "Create Account" button clicked successfully – Pass

TC-10: Verify "ACCOUNT CREATED!" message.
Result: "ACCOUNT CREATED!" message displayed – Pass

TC-11: Click "Continue" button to proceed.
Result: "Continue" button clicked; navigated to account page – Pass

TC-12: Verify "Logged in as Kimberly Test" is visible.
Result: Logged in verification successful – Pass

TC-13: Click "Delete Account" button with retry mechanism.
Result: "Delete Account" button clicked successfully – Pass

TC-14: Verify "ACCOUNT DELETED!" message and click "Continue."
Result: "ACCOUNT DELETED!" message displayed; "Continue" button clicked – Pass

**Bugs/Issues Found:**

Intermittent Verification Errors: Occasional delays in verifying messages such as "ACCOUNT CREATED!" and "ACCOUNT DELETED!" due to page load times. However, all steps were successfully executed, and functionality was not impacted.

**Conclusion:**
The test validated the script's ability to create and delete an account on the Automation Exercise website. It effectively handled consent popups, dynamically generated unique emails, and incorporated retry mechanisms for robust execution. Minor verification timing issues were noted but did not affect the overall outcome. The script is reliable for automated testing on this website.