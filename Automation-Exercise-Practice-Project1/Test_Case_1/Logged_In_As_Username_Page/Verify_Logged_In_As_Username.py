from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_logged_in_as_user_visibility():
    # Verify that 'Logged in as username' is visible
    try:
        login_as_user_text = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
        if login_as_user_text.text == "Logged in as Rahat":
            print("Logged in as Rahat successful")
        else:
            print("Login page not Okay")
    except Exception as e:
        print("Login page Exception: ", type(e).__name__)
