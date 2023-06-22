from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_password_field():
    # checking password field click
    try:
        password_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
        password_field.send_keys("23232323")
        print("Password entered successfully!")
    except Exception as e:
        print("Password field click exception: ", type(e).__name__)
