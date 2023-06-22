from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_signup_btn():
    # Click on 'Signup / Login' button
    try:
        signup_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='\/login']",)))
        signup_btn.click()
        print("Signup button clicked successfully!")
    except Exception as e:
        print("Sign up button click exception: ", type(e).__name__)