from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_continue_btn_click():
    # Continue button click checking
    try:
        new_continue_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
        new_continue_btn.click()
        print("Continue button clicked successfully!")
    except Exception as e:
        print("Continue button Exception: ", type(e).__name__)
