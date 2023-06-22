from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_new_user_signup_page():
    # Verify 'New User Signup!' is visible
    assert "https://automationexercise.com/login" in driver.current_url, f"Signup URL mismatched!"
    print("New User Sign up page opened successfully!")
