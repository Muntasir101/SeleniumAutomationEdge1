from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_click_on_create_account_btn():
    # Click on 'Create Account' button
    try:
        create_account_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .btn-default")))
        create_account_btn.click()
        print("Create Account button clicked successfully!")
    except Exception as e:
        print("Create Account button click exception: ", type(e).__name__)
