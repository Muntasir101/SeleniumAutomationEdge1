from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_account_information_page_visibility():
    # verifying "ENTER ACCOUNT INFORMATION" page visibility
    assert "https://automationexercise.com/signup" in driver.current_url, f"Account Info URL mismatched!"
    print("Account Information page opened successfully!")
