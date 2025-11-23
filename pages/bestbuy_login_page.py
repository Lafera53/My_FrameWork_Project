"""
Best Buy Login Page Object Model
Learning: Page Object Model separates page elements and actions from test code
"""

from pages.base_page import BasePage


class BestBuyLoginPage(BasePage):
    """Learning: This class represents the Best Buy login page and its elements"""

    def __init__(self, page):
        """Initialize the login page with Playwright page object"""
        super().__init__(page)
        self.page_title = "h1"

        # Learning: Define all locators at the top for easy maintenance
        # Locators for login page elements
        self.account_button = "text=Account"  # Top navigation account button
        self.sign_in_button = "text=Sign In"  # Sign in button from dropdown
        self.email_input = "input[type='email']"  # Email input field
        self.password_input = "input[type='password']"  # Password input field
        self.submit_button = "button[type='submit']"  # Login submit button
        self.error_message = ".error-message"  # Error message container
        self.create_account_link = "text=Create an Account"  # Create account link
        self.forgot_password_link = "text=Forgot your password?"  # Password reset link

    def navigate_to_login(self):
        """Learning: Navigate to Best Buy login page"""
        self.logger.info("Navigating to Best Buy login page")
        self.navigate("https://www.bestbuy.com/identity/signin")

    def click_account_button(self):
        """Click the Account button in top navigation"""
        self.logger.info("Clicking Account button")
        self.click_element(self.account_button)

    def click_sign_in(self):
        """Click the Sign In button from account dropdown"""
        self.logger.info("Clicking Sign In button")
        self.click_element(self.sign_in_button)

    def enter_email(self, email):
        """Learning: Enter email into the email input field"""
        self.logger.info(f"Entering email: {email}")
        self.fill_input(self.email_input, email)

    def enter_password(self, password):
        """Learning: Enter password into the password input field"""
        self.logger.info("Entering password")
        self.fill_input(self.password_input, password)

    def click_submit(self):
        """Click the submit/login button"""
        self.logger.info("Clicking submit button")
        self.click_element(self.submit_button)

    def login(self, email, password):
        """
        Learning: This is a composite action that performs complete login
        Combines multiple steps into one reusable method
        """
        self.logger.info(f"Performing login with email: {email}")
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()

    def is_error_message_visible(self):
        """Learning: Check if error message is displayed after login attempt"""
        return self.is_element_visible(self.error_message)

    def get_error_message(self):
        """Get the error message text"""
        self.logger.info("Getting error message text")
        return self.get_element_text(self.error_message)

    def click_create_account(self):
        """Click the Create Account link"""
        self.logger.info("Clicking Create Account link")
        self.click_element(self.create_account_link)

    def click_forgot_password(self):
        """Click the Forgot Password link"""
        self.logger.info("Clicking Forgot Password link")
        self.click_element(self.forgot_password_link)

    def verify_login_page_loaded(self):
        """Learning: Verify that the login page has loaded correctly"""
        self.logger.info("Verifying login page is loaded")
        return self.is_element_visible(self.email_input)