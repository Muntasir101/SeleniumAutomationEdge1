from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_signup_btn_click():
    # Click on 'Signup' button
    try:
        new_signup_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))
        new_signup_btn.click()
        print("New Signup button clicked successfully!")
    except Exception as e:
        print("New Sign up button click exception: ", type(e).__name__)
