# Test Report: Browse Through Programs on Masterschool Website
**Test Objective:**
Verify that the script successfully opens the Masterschool website, locates and clicks the “Browse Programs” link, and displays the list of available programs.

**Test Cases Executed:**

- TC-01: Open the Masterschool website.

Result: Website opened successfully – Pass
- TC-02: Accept the cookie consent popup if it appears.
Result: Cookie consent handled (clicked if present; skipped if not) – Pass

- TC-03: Locate the “Browse Programs” link using link text or XPath as a backup.
Result: Link located and clicked – Pass

- TC-04: Confirm that clicking the link leads to the correct program list page.
Result: Program list page loaded successfully – Pass

- TC-05: Verify that the list of programs is displayed on the page.
Result: Program names printed successfully, indicating programs were found – Pass

**Bugs/Issues Found:**
No issues encountered. The script performed all actions as expected.

**Conclusion:**
The test validated that the "Browse Programs" link on the Masterschool website can be located, clicked, and that it navigates to the correct program list page. The script effectively handles both the cookie consent popup and locator flexibility, enhancing its reliability.