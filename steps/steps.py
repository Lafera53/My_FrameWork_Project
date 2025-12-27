from behave import step

from pages.login_page import LoginPage


@step("I am on the BestBuy {env} environment login page")
def navigate_to_login_page(context,env):
    # Map environment names to their respective URLs
    environments = {
        'prod': 'https://www.bestbuy.com/home'
    }

    # Get the URL for the specified environment
    url = environments.get(env.lower())
    if not url:
        raise ValueError(f"Unknown environment: {env}. Available: prod")

    # Navigate to the appropriate login page
    context.page.goto(url)
    # Wait for page to load completely
    context.page.wait_for_load_state('networkidle')


@step('I enter "{text}" in the email field')
def input_email(context, text):
    login_page = LoginPage(context.page)
    login_page.enter_email(text)

@step("I click the continue button")
def click_continue_button(context):
    login_page = LoginPage(context.page)
    login_page.click_continue_button()


@step("I select Use password option")
def click_use_password_radio_button(context):
    login_page = LoginPage(context.page)
    login_page.click_use_password_radio_button()


@step('I enter "{text}" in the password field')
def input_password(context, text):
    login_page = LoginPage(context.page)
    login_page.enter_password(text)


@step("I click the signin option continue button")
def signin_option_continue_button(context):
    login_page = LoginPage(context.page)
    login_page.click_signin_options_continue_button()


@step("Wait for {sec} seconds")
def wait_for_sec(context, sec):
    context.page.wait_for_timeout(int(sec) * 1000)

