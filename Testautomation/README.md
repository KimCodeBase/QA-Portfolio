<h1 align="center">TestAutomation Folder</h1>

<p align="center">This folder contains the automated test scripts and reports for various tasks involving Selenium WebDriver and PyTest. Each test demonstrates different aspects of automation, such as handling web elements, interacting with forms, and using locators. The folder follows best practices, including modularization and the Page Object Model (POM).</p>

<hr>

<h2>📂 Folder Structure</h2>

<ul>
    <li><strong>POM/</strong>: Contains Page Object Model classes that encapsulate page-specific locators and actions.</li>
    <li><strong>TestCases/</strong>: Includes individual test scripts demonstrating various automation tasks.</li>
    <li><strong>TestReports/</strong>: Contains detailed execution reports for each test case, documenting the steps, results, and conclusions.</li>
</ul>

<hr>

<h2>🚀 How to Run the Tests</h2>

<ol>
    <li>
        <strong>Prerequisites:</strong>
        <ul>
            <li>Install Python 3.8+.</li>
            <li>Install dependencies:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Ensure <code>chromedriver</code> is installed and the path is added to the <code>.env</code> file as <code>CHROME_DRIVER_PATH</code>.</li>
        </ul>
    </li>
    <li>
        <strong>Run Tests with PyTest:</strong>  
        Navigate to the <code>TestCases</code> folder and execute:
        <pre><code>pytest</code></pre>
    </li>
    <li>
        <strong>View Test Reports:</strong>  
        Test reports for each script can be found in the <code>TestReports</code> folder.
    </li>
</ol>

<hr>

<h2>📜 Test Cases Overview</h2>

<h3>1. <a href="./TestCases/pytest_example_test.py">Google Search Automation</a></h3>
<ul>
    <li><strong>Objective:</strong> Automate a Google search for the term "ISTQB."</li>
    <li><strong>Steps:</strong>
        <ol>
            <li>Open Google.</li>
            <li>Handle consent popup.</li>
            <li>Input "ISTQB" in the search bar.</li>
            <li>Click the first search result.</li>
            <li>Verify the page title contains "ISTQB."</li>
        </ol>
    </li>
    <li><strong>Test Report:</strong> <a href="./TestReports/pytest_report.md">View Report</a></li>
</ul>

<h3>2. <a href="./TestCases/test_automation.py">Browse Through Programs on Masterschool Website</a></h3>
<ul>
    <li><strong>Objective:</strong> Automate navigation to the Masterschool website's "Browse Programs" page.</li>
    <li><strong>Steps:</strong>
        <ol>
            <li>Open the Masterschool website.</li>
            <li>Handle cookie popups.</li>
            <li>Locate and click the "Browse Programs" link.</li>
            <li>Verify the program list appears.</li>
        </ol>
    </li>
    <li><strong>Test Report:</strong> <a href="./TestReports/TestReport_browse_trough_programms.md">View Report</a></li>
</ul>

<h3>3. <a href="./TestCases/test_google_dynamic_dropdown.py">Google Search with Dynamic Dropdown</a></h3>
<ul>
    <li><strong>Objective:</strong> Automate selecting the first option from Google's dynamic dropdown while searching for "ISTQB."</li>
    <li><strong>Steps:</strong>
        <ol>
            <li>Open Google.</li>
            <li>Enter "ISTQB" in the search bar.</li>
            <li>Use keyboard interactions to select the first result.</li>
            <li>Verify navigation to the results page.</li>
        </ol>
    </li>
    <li><strong>Test Report:</strong> <a href="./TestReports/TestReport_Google_searchautomation.md">View Report</a></li>
</ul>

<h3>4. <a href="./TestCases/test_register_user.py">User Registration on Automation Exercise Website</a></h3>
<ul>
    <li><strong>Objective:</strong> Automate the process of creating and deleting a user account.</li>
    <li><strong>Steps:</strong>
        <ol>
            <li>Navigate to the Automation Exercise website.</li>
            <li>Register a new user with dynamically generated details.</li>
            <li>Verify account creation.</li>
            <li>Delete the account and verify deletion.</li>
        </ol>
    </li>
    <li><strong>Test Report:</strong> <a href="./TestReports/TestReport_User_Register.md">View Report</a></li>
</ul>

<h3>5. <a href="./TestCases/test_wikipedia_search.py">Wikipedia Search Automation</a></h3>
<ul>
    <li><strong>Objective:</strong> Automate searching for "Selenium WebDriver" on Wikipedia.</li>
    <li><strong>Steps:</strong>
        <ol>
            <li>Navigate to the Wikipedia homepage.</li>
            <li>Input "Selenium WebDriver" in the search bar.</li>
            <li>Submit the search query.</li>
            <li>Verify that the results page contains "Selenium (software)."</li>
        </ol>
    </li>
    <li><strong>Test Report:</strong> <i>Pending Completion</i></li>
</ul>

<hr>
