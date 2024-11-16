<h1 align="center">📂 TestAutomation Folder</h1>

<p align="center">
    This folder contains a series of Selenium-based automation scripts that demonstrate a variety of test automation tasks, including web element interactions, dynamic element handling, and the implementation of the Page Object Model (POM) pattern.
</p>

<hr>

<h2>📁 Folder Structure</h2>

<ul>
    <li><strong>POM (Page Object Model)</strong>: Contains Python classes that encapsulate locators and methods for interacting with specific web pages, promoting reusability and maintainability in automation scripts.</li>
    <li><strong>TestCases</strong>: Includes test scripts that utilize the POM classes to perform various automated test scenarios. These scripts cover tasks like dynamic dropdown handling, form submission, and login flows.</li>
</ul>

<hr>

<h2>🧪 Key Tasks Demonstrated</h2>

<h3>Task 1: Automate Google Search with Dynamic Dropdown</h3>
<ul>
    <li>Launches the Google homepage and verifies the search bar visibility.</li>
    <li>Enters a search term, selects the first suggestion dynamically, and verifies navigation to the results page.</li>
</ul>

<h3>Task 2: Automate User Registration</h3>
<ul>
    <li>Automates the entire user registration flow on <code>http://automationexercise.com</code>, including form filling, account creation, and deletion.</li>
    <li>Uses robust locators to handle dynamic elements like pop-ups and consent banners.</li>
</ul>

<h3>Task 3: Product Search Automation</h3>
<ul>
    <li>Navigates to the "All Products" page and searches for a specific product.</li>
    <li>Verifies that the search results are displayed correctly.</li>
</ul>

<h3>Task 4: Refactoring with the Page Object Model</h3>
<ul>
    <li>Implements the POM pattern to separate test logic from web element interactions.</li>
    <li>Includes a class for the Wikipedia search page, encapsulating methods to interact with its elements.</li>
</ul>

<h3>Task 5: Exploring PyTest</h3>
<ul>
    <li>Sets up PyTest to execute test cases efficiently and validates the use of fixtures for browser management.</li>
    <li>Demonstrates parameterized test cases for robust and reusable test flows.</li>
</ul>

<hr>

<h2>🔧 How to Use</h2>

<h3>Setup</h3>
<ul>
    <li>Ensure <strong>Python 3.8+</strong> is installed on your machine.</li>
    <li>Install the required dependencies by running:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Download ChromeDriver and ensure its path is configured in your <code>.env</code> file:
        <pre><code>CHROME_DRIVER_PATH=/path/to/chromedriver</code></pre>
    </li>
    <li>Optional: For local HTML file testing, add its path to the <code>.env</code> file:
        <pre><code>HTML_FILE_PATH=/path/to/sample.html</code></pre>
    </li>
</ul>

<h3>Running the Tests</h3>
<p>To execute all test cases in the <code>TestCases</code> folder, run:</p>
<pre><code>pytest TestAutomation/TestCases/</code></pre>
<p>To run individual test scripts, navigate to their location and execute:</p>
<pre><code>pytest test_file_name.py</code></pre>

<hr>

<h2>📈 Skills Highlighted</h2>
<ul>
    <li><strong>Dynamic Element Handling:</strong> Techniques to interact with dynamic dropdowns and web elements.</li>
    <li><strong>End-to-End Automation:</strong> Comprehensive workflows for user registration, search functionalities, and login processes.</li>
    <li><strong>Page Object Model (POM):</strong> Clean and maintainable structure for test scripts.</li>
    <li><strong>PyTest Integration:</strong> Efficient test execution and reporting with fixtures and assertions.</li>
    <li><strong>Locator Strategies:</strong> Advanced use of XPath, CSS selectors, and other locators.</li>
</ul>

<hr>

<h2>💡 Notes</h2>
<ul>
    <li>All scripts include proper exception handling and wait mechanisms to ensure stability.</li>
    <li>Test reports can be generated using PyTest plugins for detailed insights into test results.</li>
    <li>Refer to the <strong>TestReports</strong> folder for sample test results and screenshots.</li>
</ul>

<p>Thank you for exploring the <strong>TestAutomation</strong> folder! These tasks are designed to demonstrate key automation skills and best practices.</p>
