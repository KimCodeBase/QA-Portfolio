1. User Registration and Login
   
Test Cases:

Test Case 1: Verify that a new user can create an account with valid email and password.

Input: Enter a valid email and a password.
Expected Outcome: Account creation successful, user is logged in.

Test Case 2: Verify that an error message is shown if the email is in an incorrect format.

Input: Enter an email without "@" (e.g., "useremail.com").
Expected Outcome: Error message "Invalid email format."

Test Case 3: Verify that a user can log in with correct credentials.

Input: Enter the correct email and password.
Expected Outcome: User is logged in successfully.
Test Case 4: Verify that an error message is shown if the wrong password is entered.

Input: Enter a valid email and an incorrect password.
Expected Outcome: Error message "Incorrect password."

2. Product Search and Filtering
Test Cases:

Test Case 1: Verify that the user can search for a product by name.

Input: Enter "Celery" in the search bar.
Expected Outcome: A list of products containing "Celery" is displayed.

Test Case 2: Verify that the user sees a message if no products match the search term.

Input: Enter "Xyzabc" in the search bar.
Expected Outcome: Message "No products found" is displayed.

Test Case 3: Verify that the price filter works correctly.

Input: Set price filter to $10 - $20.
Expected Outcome: Only products priced between $10 and $20 are displayed.

3. Adding Products to the Cart
Test Cases:

Test Case 1: Verify that a user can add a product to the cart.

Input: Click "Add to Cart" on a product page.
Expected Outcome: Product is added to the cart.
Test Case 2: Verify that the cart updates when multiple quantities are added.

Input: Add 3 units of the same product.
Expected Outcome: The cart shows 3 units of the product.
Test Case 3: Verify that an error is shown when trying to add 0 quantity.

Input: Set quantity to 0 and try to add to cart.
Expected Outcome: Error message "Quantity must be at least 1."

4. Checkout Process
Test Cases:

Test Case 1: Verify that the user can proceed to checkout with products in the cart.

Input: Click "Checkout" with items in the cart.
Expected Outcome: User is directed to the checkout page.

Test Case 2: Verify that the user can complete a purchase with valid payment details.

Input: Enter valid credit card information.
Expected Outcome: Payment is successful, order confirmation is displayed.

Test Case 3: Verify that an error message is shown if the payment method is invalid.

Input: Enter an expired credit card.
Expected Outcome: Error message "Payment failed."

5. Adding Favorites
Test Cases:

Test Case 1: Verify that a user can add a product to favorites.

Input: Click "Add to Favorites" on a product page.
Expected Outcome: Product is added to the favorites list.
Test Case 2: Verify that an error is shown if trying to add a product to favorites without logging in.

Input: Try to add a product to favorites without being logged in.
Expected Outcome: Prompt to log in or error message.

