from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_account_creation_successful_page():
    # verifying "ACCOUNT CREATION SUCCESSFUL" page visibility
    assert "https://automationexercise.com/account_created" in driver.current_url, f"Account Creation URL mismatched!"
    print("ACCOUNT CREATION SUCCESSFUL page opened successfully!")
