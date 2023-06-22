from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_delete_account_btn_click():
    # Delete Account button click checking
    try:
        delete_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a")))
        delete_btn.click()
        print("Delete button clicked successfully!")
    except Exception as e:
        print("Delete button Exception: ", type(e).__name__)
