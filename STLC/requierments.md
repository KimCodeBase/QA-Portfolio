<h2><b>The software</b></h2>
Webshop, with the following basic functionalities:<br>
- Register and login functionality<br>
- Searching for products, sorting on price, categories of products<br>
- Add products to favorites<br>
- Add products to basket<br>
Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)<br>
<h2><b>New features</b></h2>
<p><b>1. Product Rating System</b></p>
<p>Vague Requirement: </p>Users should be able to rate products with a 5-star system and have the option to add written feedback.<br>
<p><b>Questions:</b></p>
- Should users be able to edit or delete their ratings and feedback?<br>
- Should there be any restrictions on who can rate a product (e.g., only users who purchased the product)?<br>
- How should the ratings and feedback be displayed on the product page?<br>
- Are there any moderation requirements for the written feedback?<br>
<h2><b>Detailed Requirement:</b></h2> Users can rate products using a 5-star system and add written feedback up to 500 characters. Only users who have purchased the product can leave a rating and feedback. Users can edit or delete their ratings and feedback. Ratings and feedback will be displayed under the product description with the most recent at the top. Feedback will eventually be moderated for inappropriate content using an automated filtering system and manual review, but this is not part of the story now.
<p><b>2. Age Verification for Alcoholic Products</b></p>
<p><b>Vague Requirement:</b></p> Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.
<p><b>Questions:</b></p>
-How should the age be verified (e.g., simple input, date picker, integration with an ID verification system)?<br>
-What should happen if the user inputs an age below 18?<br>
-Should the age verification modal appear every time the user visits the alcoholic products category or just once?<br>
<p><b>Detailed Requirement:</b></p> 
A modal will appear asking the user to confirm if they are 18+ by inputting their birth date in the format DD/MM/YYYY. If the user inputs an age below 18, they will be denied access to the alcoholic products category and redirected to the homepage. The age verification modal will appear only once per session.
<p><b>3. Shipping Cost Changes</b></p>
Vague Requirement:<br>
Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.
<p><b>Questions:</b></p>
-What is the new shipping fee for orders below the specified amount?<br>
-Is the free shipping threshold inclusive or exclusive of taxes and other fees?<br>
-Should the shipping cost information be displayed during the checkout process?<br>
-Are there any exceptions to the shipping cost changes (e.g., specific regions, product types)?<br>
<p><b>Detailed Requirement:</b></p>
Orders of €20 and above will qualify for free shipping. Orders below €20 will incur a shipping fee of €5. The free shipping threshold is inclusive of taxes but exclusive of other fees. Shipping cost information should be clearly displayed during the checkout process. There are no exceptions; the policy applies to all regions and product types.
