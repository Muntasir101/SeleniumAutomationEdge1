from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_account_deletion_verification():
    # Checking if Account Deletion Successful or not
    try:
        delete_text = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
        if delete_text.text == "ACCOUNT DELETED!":
            print("Deleted text checked successfully")
        else:
            print("Delete page not Okay")
    except Exception as e:
        print("Delete page Exception: ", type(e).__name__)

